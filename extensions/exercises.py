"""
Add directives for writing exercises and solutions. This extension supports:

   .. exercise:: Name

       Any content here...

       .. solution

           Solution takes place here...

To summarize:

    - Exercises are automatically numbered "Exercise 1.1" (section number + exercise number)
    - If a `.. exercises::`, the exercises is mentionned, the `exercise` directive
      is replaced with a reference to the exercise
    - Solutions can be hidden with `:hidden:`
"""
from collections import OrderedDict
import os
from os import path
import sphinx.locale
from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx import addnodes
from sphinx.directives import SphinxDirective
from sphinx.environment.collectors import EnvironmentCollector
from sphinx.locale import _
from sphinx.util import logging, texescape
from sphinx.util.template import LaTeXRenderer
from sphinx.locale import get_translation

package_dir = path.abspath(path.dirname(__file__))

_ = get_translation(__name__)

logger = logging.getLogger(__name__)

latex_preamble = r"""
%% Support for exercises
%
\newcommand{\listofexercises}{<%= listofexercises %>}
\newlistof{exercise}{exp}{\listofexercises}

%% Restart counter at each new chapter
\makeatletter
\@addtoreset{exercise}{chapter}
\makeatother

%% Exercise environment
\newenvironment{exercise}[1][]{%
    \refstepcounter{exercise}
    \par\addvspace{\baselineskip}\noindent\textbf{<%= exercise %> \thechapter.\theexercise} {#1}
    \par
    \addcontentsline{exp}{exercise}{%
        <%= exercise %> \thechapter.\theexercise
        \ifx&#1&\else\ -- #1\fi
    }\par
}{%
}
"""

class exercise_title(nodes.strong, nodes.Element):
    """ Title of exercises and solutions """


class exercise(nodes.Admonition, nodes.Element):
    """ An exercise """


class solution(nodes.Admonition, nodes.Element):
    """ A solution to an exercise """


class solutions(nodes.General, nodes.Element):
    """ Set of solutions. The solutions are declared in a exercise
    block, but they can be grouped in the same section. """


class table_of_exercises(nodes.General, nodes.Element):
    """ List of all exercises """


class SolutionsDirective(SphinxDirective):
    """ Directive replaced with all exercises found in all documents:
        Section number, subsection, exercises...
    """
    def run(self):
        self.env.exercises_all_solutions_docname = self.env.docname
        return [solutions()] # Processed once the toctree is built.


class ExerciseDirective(SphinxDirective):
    """ An exercise """
    final_argument_whitespace = True
    has_content = True
    optional_arguments = 1

    def run(self):
        self.assert_has_content()

        # Destination for a reference to this exercise
        target_id = 'exercise-%d' % self.env.new_serialno('sphinx.ext.exercises')
        target_node = nodes.target('', '', ids=[target_id])

        exercise_node = exercise(self.content, **self.options)

        # Exercise number not known before the toctree is resolved.
        # This title will be modified later.
        exercise_node += exercise_title(_('Exercise'), _('Exercise'))

        # par = nodes.paragraph()
        # exercise_node += par

        # Allow for parsing content as ReST
        self.state.nested_parse(self.content, self.content_offset, exercise_node)

        # Populate exercise pool
        exercise_node['lineno'] = self.lineno
        exercise_node['docname'] = self.env.docname
        exercise_node['title'] = self.arguments[0] if self.arguments else ''
        data = {
            'lineno': self.lineno,
            'docname': self.env.docname,
            'node': exercise_node,
            'title': self.arguments[0] if self.arguments else '',
            'target': target_node,
        }
        self.env.exercises_all_exercises.append(data)
        self.env.exercises_exercises_map[(self.env.docname, target_id)] = data

        return [target_node, exercise_node]


class SolutionDirective(BaseAdmonition):
    node_class = solution

    def run(self):
        if not self.arguments:
            self.arguments.append(_('Solution'))

        return super().run()


def env_before_read_docs(app, env, docnames):
    """ Creates the meta data containers. """
    del app, docnames # Unused
    if not hasattr(env, 'exercises_all_exercises'):
        env.exercises_all_exercises = []
    if not hasattr(env, 'exercises_exercises_map'):
        env.exercises_exercises_map = {}


class ExercisesCollector(EnvironmentCollector):
    """ Once the document is parsed, we can identify the chapter numbers
    and add some more information to the exercise pool:
      - Number of exercise (chapter is number[0])
      - Label to display
      - Node with content
    """
    def clear_doc(self, app, env, docname):
        pass

    def process_doc(self, app, doctree):
        pass

    def merge_other(self, app, env, docnames, other):
        pass

    def get_updated_docs(self, app, env):
        """ When a document is updated, the toctree is traversed to
        find new exercises.
        """
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
        ids = node['ids']

        # Get exercise node previously created.
        # For some reason attributes cannot be set on the node itself
        solution_nodes = node.traverse(solution)
        number = env.toc_fignumbers.get(docname, {}).get('exercise', {}).get(ids[0])
        node_id = (docname, ids[0])
        env.exercises_exercises_map[node_id].update({
            'number': number,
            'label': app.config.numfig_format['exercise'] % '.'.join(map(str, number)),
            'solution': solution_nodes[0] if len(solution_nodes) == 1 else None
        })


def get_reference(meta):
    return '/'.join(['exercise'] + list(map(str, meta['number'])))


def process_exercise_nodes(app, doctree, fromdocname):
    """ Once the doctree is resolved, the exercises are injected where
    they need to.
    """

    # Copy saved arguments to nodes, restore node pointers
    for node in doctree.traverse(exercise):
        node_id = (node['docname'], node['ids'][0])
        meta = app.env.exercises_exercises_map[node_id]
        node['label'] = meta['label']
        node['number'] = meta['number']
        node['title'] = meta['title']
        meta['node'] = node

    # Sort exercises in ascending order
    all_exercises = app.env.exercises_all_exercises
    all_exercises.sort(key=lambda ex: ex['number'])

    # Regroup exercises organized by chapters
    hierarchy = OrderedDict()
    for ex in all_exercises:
        chapter = ex['number'][0]
        if chapter not in hierarchy:
            hierarchy[chapter] = []
        hierarchy[chapter].append(ex)

    # Update exercise titles
    for node in doctree.traverse(exercise):
        label = node['label']
        if node['title']:
            label += ' ' + node['title']
        node.children[0].replace_self(
            exercise_title(label, label))

    # Populate the solutions directive
    for node in doctree.traverse(solutions):
        content = []
        for chapter, exs in hierarchy.items():
            # Ignore chapters without solutions
            if not [e for e in exs if e['solution']]:
                continue

            # Create a section per chapter
            section = nodes.section(ids=[f'solution-chapter-{chapter}'], auto=0)
            name = _('Chapter') + ' ' + str(chapter)
            section.append(nodes.title(name, name))
            content.append(section)
            # Insert the solutions
            for ex in [e for e in exs if e['solution']]:
                description = ex['label']

                para = nodes.paragraph()
                title = exercise_title(description, description)
                if app.builder.format in ['latex', 'html']:
                    ref = nodes.reference('', '')
                    ref['refdocname'] = ex['docname']
                    ref['refuri'] = app.builder.get_relative_uri(fromdocname, ex['docname'])
                    ref['refuri'] += '#' + ex['target']['refid']
                    ref.append(title)
                    title = ref
                para.append(title)
                content.append(para)
                content.extend(ex['solution'].children)

        node.replace_self(content)

    # Remove solution from the exercises
    for ex in doctree.traverse(exercise):
        ex.children = list(filter(lambda x: not isinstance(x, solution), ex.children))

def build_finished(app, env):
    # Inject LaTeX header
    if env.exercises_all_exercises and hasattr(app.builder, 'context'):
        inject_latex_header(app, app.builder.context)

def inject_latex_header(app, context):
    context['preamble'] += '\n' + r"%% BEGIN injection for extension exercises"
    render = LaTeXRenderer()
    render.env.comment_start_string = '<#'
    render.env.comment_end_string = '<#'
    context['preamble'] += render.render_string(latex_preamble, {
        'exercise': _('Exercise'),
        'listofexercises': _('List of Exercises')
    })
    context['preamble'] += '\n' + r"%% END injection for extension exercises"


def check_config(app, config):
    # Enable numfig, required for this extension
    if not config.numfig:
        logger.error('Numfig config option is disabled, setting it to True')
        config.numfig = True

    config.numfig_format.update({'exercise': _('Exercise %s')})


def purge(app, env, docname):
    del app
    if not hasattr(env, 'exercises_all_exercises'):
        return
    env.exercises_all_exercises = [
        ex for ex in env.exercises_all_exercises
        if ex['docname'] != docname
    ]

def visit_html_exercise(self, node, name=''):
    self.body.append(self.starttag(node, 'div', CLASS=('exercise ' + name)))
    if hasattr(node, 'exnum'):
        self.body.append('secnum: %s' % str(node.exnum))

def depart_html_exercise(self, node=None):
    self.body.append('</div>\n')

def visit_latex_exercise(self, node, name=''):
    self.body.append('\n\\begin{exercise}')
    title = texescape.escape(node['title'])
    if node['title']:
        self.body.append('[' + title + ']')

def depart_latex_exercise(self, node=None):
    self.body.append('\\end{exercise}\n')

def visit_html_solution(self, node, name=''):
    self.visit_admonition(node, name='solution')


def depart_html_solution(self, node=None):
    self.depart_admonition(node)


def visit_latex_solution(self, node, name=''):
    self.visit_admonition(node)


def depart_latex_solution(self, node=None):
    self.depart_admonition(node)


def no_visit(self, node=None):
    del node # unused


def visit_exercise_title(self, node):
    self.visit_strong(node)


def depart_exercise_title(self, node):
    self.depart_strong(node)


def visit_latex_exercise_title(self, node):
    if isinstance(node.parent, exercise):
        raise nodes.SkipNode
    else:
        self.visit_strong(node)


def depart_latex_exercise_title(self, node):
    if isinstance(node.parent, exercise):
        raise nodes.SkipNode
    else:
        self.depart_strong(node)

def setup(app):
    no_visits = (no_visit, no_visit)

    app.add_message_catalog(__name__, path.join(package_dir, 'locales'))

    app.add_enumerable_node(exercise, 'exercise',
                            html=(visit_html_exercise, depart_html_exercise),
                            latex=(visit_latex_exercise, depart_latex_exercise),
                            man=no_visits)

    app.add_node(solution,
                 html=(visit_html_solution, depart_html_solution),
                 latex=(visit_latex_solution, depart_latex_solution),
                 man=no_visits)

    app.add_node(exercise_title,
                 html=(visit_exercise_title, depart_exercise_title),
                 latex=(visit_latex_exercise_title, depart_latex_exercise_title),
                 man=no_visits)

    sphinx.locale.admonitionlabels['solution'] = _('Solution')

    app.add_directive('exercise', ExerciseDirective)
    app.add_directive('solution', SolutionDirective)
    app.add_directive('exercises-solutions', SolutionsDirective)

    app.connect('config-inited', check_config)
    app.connect('env-before-read-docs', env_before_read_docs)
    app.connect('doctree-resolved', process_exercise_nodes)
    app.connect('env-purge-doc', purge)
    app.connect('env-updated', build_finished)
    app.add_env_collector(ExercisesCollector)

    app.add_latex_package('tocloft')
    app.add_latex_package('xparse')

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
