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
from os import path
import sphinx.locale
from collections import defaultdict
from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx.directives import SphinxDirective
from sphinx.environment.collectors import EnvironmentCollector
from sphinx.locale import _
from sphinx.util import logging, texescape
from sphinx.util.template import LaTeXRenderer
from sphinx.locale import get_translation
from sphinx.writers.html5 import HTML5Translator
from sphinx.transforms import SphinxTransform
from sphinx.errors import NoUri

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

class unnumbered_title(nodes.title):
    """ Regular title without numbering """

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
        # To know which document to rebuild if an exercise has changed.
        vars(self.env).setdefault('exercises_all_solutions', set()).add(self.env.docname)
        return [solutions()]


class ExerciseDirective(SphinxDirective):
    """ An exercise """
    final_argument_whitespace = True
    has_content = True
    optional_arguments = 1

    def run(self):
        self.assert_has_content()

        # Unique exercise identifier (each document)
        serial_no = self.env.new_serialno('sphinx.ext.exercises')
        target = nodes.target('', '', ids=[f'{self.name}-{serial_no}'])

        # Build new exercise
        exercise_node = exercise(self.content, *[
            nodes.rubric(_('Exercise'), _('Exercise'))
        ], ids=[f'{self.name}-{serial_no}'], **self.options)

        # Recursively parse the exercise's content
        self.state.nested_parse(self.content, self.content_offset, exercise_node)

        # Save metadata
        exercise_node.update_all_atts({
            'title': self.arguments[0] if self.arguments else ''
        }, and_source=True)

        # Get source line/code for later
        exercise_node.source = self.env.docname
        exercise_node.line = self.lineno

        return [target, exercise_node]


class SolutionDirective(BaseAdmonition):
    node_class = solution

    def run(self):
        if self.arguments:
            logger.warn("Solutions doesn't require arguments!")
        self.arguments.append(_('Solution'))
        return super().run()


class Visitors:
    @classmethod
    def get_pair(self, name):
        return (
            getattr(self, 'visit_' + name, self.no_visit),
            getattr(self, 'depart_' + name, self.no_visit)
        )

    def no_visit(self, *args, **kwargs):
        pass

class HTMLVisitors(Visitors):
    name = 'html'

    def visit_exercise(self, node, name=''):
        self.body.append('<div>\n')
        if hasattr(node, 'exnum'):
            self.body.append('secnum: %s' % str(node.exnum))

    def depart_exercise(self, node=None):
        self.body.append('</div>\n')

    def visit_solution(self, node, name=''):
        self.visit_admonition(node, name='solution')

    def depart_solution(self, node=None):
        self.depart_admonition(node)

    def visit_exercise_title(self, node):
        self.visit_strong(node)


    def depart_exercise_title(self, node):
        self.depart_strong(node)
        self.add_permalink_ref(node, _('Permalink to this exercise'))

    def visit_unnumbered_title(self, node):
        self.visit_title(node)
        self.body.pop(-1) # Pop the section number

    def depart_unnumbered_title(self, node):
        self.depart_title(node)


class LaTeXVisitors(Visitors):
    name = 'latex'

    def visit_exercise(self, node, name=''):
        self.body.append('\n\\begin{exercise}')
        title = texescape.escape(node['title'])
        if node['title']:
            self.body.append('[' + title + ']')

    def depart_exercise(self, node=None):
        self.body.append('\\end{exercise}\n')

    def visit_solution(self, node, name=''):
        self.visit_admonition(node)

    def depart_solution(self, node=None):
        self.depart_admonition(node)

    def visit_exercise_title(self, node):
        if isinstance(node.parent, exercise):
            raise nodes.SkipNode
        else:
            self.visit_strong(node)

    def depart_exercise_title(self, node):
        if isinstance(node.parent, exercise):
            raise nodes.SkipNode
        else:
            self.depart_strong(node)

    def visit_unnumbered_title(self, node):
        self.visit_title(node)
        self.body.append(self.body.pop(-1).replace('section', 'section*'))

    def depart_unnumbered_title(self, node):
        self.depart_title(node)


class ManVisitors(Visitors):
    name = 'man'


class Collect(EnvironmentCollector):
    """ Collect all the exercises and solutions across all documents.
    """
    def all_exercises(self, env):
        if not hasattr(env, 'exercise_exercises'):
            env.exercise_exercises = defaultdict(dict)
        return env.exercise_exercises

    def get_reference(self, node):
        return node.parent[node.parent.index(node) - 1]

    def clear_doc(self, app, env, docname):
        self.all_exercises(env)[docname] = {}
        env.exercises_counter = defaultdict(int)

    def merge_other(self, app, env, docnames, other):
        for docname in docnames:
            self.all_exercises(env)[docname] = self.all_exercises(other)[docname]

    def process_doc(self, app, doctree):
        env = app.env
        for ex in doctree.traverse(exercise):
            self.all_exercises(env)[env.docname][ex['ids'][0]] = ex

    def get_outdated_docs(self, app, env, added, changed, removed):
        exercises_document = set()
        for document in set.union(added, changed, removed):
            if self.all_exercises(env)[document]:
                exercises_document.add(document)

        if exercises_document:
            return vars(env).setdefault('exercises_all_solutions', set())
        return []

    def get_updated_docs(self, app, env):
        env.exercise_solutions = {}
        for docname, exs in env.exercise_exercises.items():
            for ids, ex in exs.items():
                sol = ex.next_node(solution)
                if sol:
                    number = env.toc_fignumbers[docname]['exercise'][ids]
                    sol['target'] = self.get_reference(ex)['refid']
                    env.exercise_solutions[number] = sol

        return []

def get_exercise_number(env, node):
    return env.toc_fignumbers[node.source]['exercise'][node['ids'][0]]

def get_exercise_title(env, node):
    number = get_exercise_number(env, node)
    return _('Exercise') + ' ' + ('.'.join(map(str, number)))

class RenameExercises(SphinxTransform):
    default_priority = 100

    def apply(self, **kwargs):
        for node in self.document.traverse(exercise):
            node.children[0][0] = nodes.Text(get_exercise_title(self.env, node))

class SolutionsChapter(SphinxTransform):
    """ Create the solution chapter by moving all the exercises
    from their original context to their new location. """
    default_priority = 100

    def get_exercise_node(self, sol):
        while sol.parent:
            if isinstance(sol.parent, exercise):
                return sol.parent
            sol = sol.parent

    def get_chapter_elements(self, chapter):
        name = _('Chapter') + ' ' + str(chapter)
        return nodes.section('',
            nodes.title(name, name),
            ids=[f'exercise-solutions-chapter-{chapter}'])

    def get_solution_elements(self, sol):
        ex = self.get_exercise_node(sol)

        try:
            refuri = self.app.builder.get_relative_uri(self.env.docname, ex.source) + '#' + ex['ids'][0]
        except NoUri:
            refuri = ''

        title_text = get_exercise_title(self.env, ex)
        return nodes.section('',
            nodes.rubric('', '',
                nodes.reference(title_text, title_text, refuri=refuri, refdocname=ex.source),
                *[nodes.Text(' - ' + ex['title'])] if ex['title'] else [],
                #classes=['caption']
            ),
            *sol.children,
            ids=['solution-' + ('.'.join(map(str, get_exercise_number(self.env, ex))))]
        )

    def build_solutions(self):
        chapter = 0
        elements = nodes.section(ids=['exercises-solutions'])
        sols = sorted(self.env.exercise_solutions.items(), key=lambda x: x[0])
        for number, sol in sols:
            if chapter != number[0]:
                chapter += 1
                context = self.get_chapter_elements(chapter)
                elements += context
            context += self.get_solution_elements(sol)
        return elements

    def apply(self, **kwargs):
        # Build the list of solutions
        for node in self.document.traverse(solutions):
            node.replace_self(self.build_solutions())

        # Remove the solutions from the document
        for node in self.document.traverse(solution):
            node.replace_self([])

def check_config(app, config):
    # Enable numfig, required for this extension
    if not config.numfig:
        logger.error('Numfig config option is disabled, setting it to True')
        config.numfig = True

    config.numfig_format.update({'exercise': _('Exercise %s')})


def build_finished(app, env):
    if env.exercise_exercises and hasattr(app.builder, 'context'):
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

def depart_rubric(self, node):
    self.add_permalink_ref(node.parent, _('Permalink to this rubric'))
    self.body.append('</p>\n')

def get_visitors(element, builders=[HTMLVisitors, LaTeXVisitors, ManVisitors]):
    return {builder.name: builder.get_pair(element) for builder in builders}

def setup(app):
    app.add_message_catalog(__name__, path.join(package_dir, 'locales'))

    sphinx.locale.admonitionlabels['solution'] = _('Solution')

    app.add_directive('exercise', ExerciseDirective)
    app.add_directive('solution', SolutionDirective)
    app.add_directive('exercises-solutions', SolutionsDirective)

    app.add_enumerable_node(exercise, 'exercise', **get_visitors('exercise'))
    app.add_node(solution, **get_visitors('solution'))
    app.add_node(exercise_title, **get_visitors('exercise_title'))
    app.add_node(unnumbered_title, **get_visitors('unnumbered_title'))

    app.connect('config-inited', check_config)
    app.connect('env-updated', build_finished)

    app.add_env_collector(Collect)
    app.add_post_transform(RenameExercises)
    app.add_post_transform(SolutionsChapter)

    app.add_latex_package('tocloft')
    app.add_latex_package('xparse')

    HTML5Translator.depart_rubric = depart_rubric

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
