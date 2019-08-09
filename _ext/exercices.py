"""
Add directives for writing exercises and solutions. This extension supports:

   .. exercise:: Name

       Any content here...

       .. solution

           Solution takes place here...

To summarize:

    - Exercises are automatically numbered "Exercise 1.1" (section number + exercise number)
    - If a `.. all-exercises::`, the exercises are mentionned where, the `exercise` directive
      is replaced with a reference to the exercise
    - Solutions can be hidden with `:hidden:`
"""
import logging

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import Hint

from sphinx.writers.html5 import HTML5Translator
from sphinx.util.console import colorize
from sphinx.locale import _
from sphinx import addnodes
from sphinx.util.docutils import SphinxDirective
from sphinx.environment.adapters.toctree import TocTree
from sphinx.environment.collectors import EnvironmentCollector
from sphinx.util import url_re

from collections import OrderedDict

logger = logging.getLogger(__name__)


class exercise(nodes.Admonition, nodes.Element):
    pass


class all_exercises(nodes.General, nodes.Element):
    pass


class solution(nodes.Admonition, nodes.Element):
    pass


class AllExercisesDirective(SphinxDirective):
    """ Directive replaced with all exercises found in all documents:
        Section number, subsection, exercises...
    """
    def run(self):
        self.env.exercises_all_exercises_docname = self.env.docname
        return [all_exercises()] # Let it process later once the toctree is built


class ExerciseDirective(SphinxDirective):
    final_argument_whitespace = True
    has_content = True
    optional_arguments = 1

    def run(self):
        self.assert_has_content()

        id = 'exercise-%d' % self.env.new_serialno('sphinx.ext.exercises#exercises')

        target_node = nodes.target('', '', ids=[id])

        node = exercise('\n'.join(self.content), **self.options)
        node += nodes.title(_('Exercise'), _('Exercise'))
        self.state.nested_parse(self.content, self.content_offset, node)

        if not hasattr(self.env, 'exercises_all_exercises'):
            self.env.exercises_all_exercises = OrderedDict()

        self.env.exercises_all_exercises[(self.env.docname, id)] = {
            'lineno': self.lineno,
            'docname': self.env.docname,
            'node': node,
            'title': self.arguments[0] if len(self.arguments) else '',
            'target': target_node,
        }

        return [target_node, node]


class SolutionDirective(Hint):
    pass


def visit_exercise(self, node, name=''):
    self.body.append(self.starttag(node, 'div', CLASS=('exercise ' + name)))
    if hasattr(node, 'exnum'): self.body.append('secnum: %s' % str(node.exnum))


def depart_exercise(self, node=None):
    self.body.append('</div>\n')


def visit_solution(self, node, name=''):
    self.body.append(self.starttag(node, 'div', CLASS=('solution')))


def depart_solution(self, node=None):
    self.depart_admonition(node)

def no_visit(self, node=None):
    pass

def get_reference(meta):
    return '/'.join(['exercise'] + list(map(str, meta['number'])))

def process_exercise_nodes(app, doctree, fromdocname):
    for node in doctree.traverse(exercise):
        para = nodes.paragraph()

        meta = app.env.exercises_all_exercises[(fromdocname, node['ids'][1])]
        description = meta['label']

        ref = nodes.reference('','')
        innernode = nodes.Text(description, description)
        ref['refdocname'] = fromdocname

        if hasattr(app.env, 'exercises_all_exercises_docname'):
            ref['refuri'] = app.builder.get_relative_uri(fromdocname, app.env.exercises_all_exercises_docname)
            ref['refuri'] += '#' + get_reference(meta)

        ref.append(innernode)
        para += ref

        node.parent.replace(node, para)

    for node in doctree.traverse(all_exercises):
        content = []
        for _, ex in sorted(app.env.exercises_all_exercises.items(), key=lambda x: x[1]['number']):
            n = ex['node']


            title = nodes.caption('', ex['label'] + ' ' + ex['title'])

            n.replace(n.children[n.first_child_matching_class(nodes.title)], title )
            n['ids'] = [get_reference(ex)]

            content.append(n)

        node.replace_self(content)


class ExercisesCollector(EnvironmentCollector):
    def clear_doc(self, app, env, docname):
        pass

    def process_doc(self, app, doctree):
        pass

    def get_updated_docs(self, app, env):
        if not hasattr(env, 'all_exercises'):
            env.all_exercises = []

        def traverse_all(app, env, docname):
            doctree = env.get_doctree(docname)

            for toc in doctree.traverse(addnodes.toctree):
                for _, subdocname in toc['entries']:
                    traverse_all(app, env, subdocname)

            for node in doctree.traverse(exercise):
                self.process_exercise(app, env, node, docname)

        traverse_all(app, env, env.config.master_doc)

        return []

    def process_exercise(self, app, env, node, docname):
        meta = env.exercises_all_exercises[(docname, node['ids'][1])]
        meta['number'] = env.toc_fignumbers.get(docname, {}).get('exercise', {}).get(node['ids'][0])
        meta['label'] = app.config.numfig_format['exercise'] % '.'.join(map(str, meta['number']))

        env.all_exercises.append(meta)


class Translator(HTML5Translator):
    def depart_caption(self, node):
        self.body.append('</span>')
        if (isinstance(node.parent, exercise)):
            self.add_permalink_ref(node.parent, _('Permalink to this exercise'))
        super().depart_caption(node)


def init_numfig_format(app, config):
    config.numfig_format.update({'exercise': _('Exercise %s')})


def setup(app):
    no_visits = (no_visit, no_visit)
    visitors = (visit_exercise, depart_exercise)

    app.add_enumerable_node(exercise, 'exercise',
        html=visitors,
        latex=no_visits,
        text=visitors,
        man=no_visits
    )

    app.add_node(solution,
        html=(visit_solution, depart_solution),
        latex=no_visits,
        man=no_visits
    )


    app.add_directive('exercise', ExerciseDirective)
    app.add_directive('solution', SolutionDirective)
    app.add_directive('all-exercises', AllExercisesDirective)

    app.connect('config-inited', init_numfig_format)
    app.connect('doctree-resolved', process_exercise_nodes)

    app.add_env_collector(ExercisesCollector)

    app.set_translator('html', Translator)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }