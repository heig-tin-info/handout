from docutils import nodes

from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from docutils.parsers.rst.directives.admonitions import Hint
from sphinx.environment.adapters.toctree import TocTree
from sphinx.environment.collectors import EnvironmentCollector
from sphinx.util import url_re

import uuid

class exercise(nodes.Admonition, nodes.Element):
    pass

class solution(nodes.Admonition, nodes.Element):
    pass

class SolutionDirective(Hint):
    pass

class ExerciceDirective(Hint):
    final_argument_whitespace = True
    has_content = True
    optional_arguments = 1

    def run(self):
        self.assert_has_content()

        text = '\n'.join(self.content)

        admonition_node = exercise(text, **self.options)
        admonition_node.signature = str(uuid.uuid5(uuid.NAMESPACE_OID, text))

        self.add_name(admonition_node)

        admonition_node.title = self.arguments[0] if len(self.arguments) > 0 else ''

        self.state.nested_parse(self.content, self.content_offset,
                                admonition_node)
        return [admonition_node]


def visit_exercise(self, node, name=''):
    number = '.'.join(map(str, self.builder.env.toc_exercises[node.signature]))

    self.body.append(self.starttag(node, 'div', CLASS=('exercise ' + name)))
    self.body.append('<h3>Exercice %s: %s</h3>' % (number, node.title))


def depart_exercise(self, node=None):
    self.body.append('</div>\n')


def visit_solution(self, node, name=''):
    self.body.append(self.starttag(node, 'div', CLASS=('solution')))


def depart_solution(self, node=None):
    self.depart_admonition(node)


class ExercisesCollector(EnvironmentCollector):

    def clear_doc(self, app: Sphinx, env: BuildEnvironment, docname):
        if not hasattr(env, 'toc_exercise_numbers'):
            env.toc_exercise_numbers =  {}

        env.toc_exercise_numbers.pop(docname, None)

    def process_doc(self, app: Sphinx, doctree: nodes.document) -> None:
        pass

    def get_updated_docs(self, app: Sphinx, env: BuildEnvironment):
        return self.assign_exercise_numbers(env)

    def assign_exercise_numbers(self, env: BuildEnvironment):
        """Assign a exercise number to each exercise under a numbered toctree."""

        rewrite_needed = []

        assigned = set()  # type: Set[str]
        old_exercise_numbers = env.toc_exercise_numbers
        env.toc_exercise_numbers = {}
        env.toc_exercises = {}
        exercise_counter = {}  # type: Dict[str, Dict[Tuple[int, ...], int]]

        def get_section_number(docname, section):
            anchorname = '#' + section['ids'][0]
            secnumbers = env.toc_secnumbers.get(docname, {})
            if anchorname in secnumbers:
                secnum = secnumbers.get(anchorname)
            else:
                secnum = secnumbers.get('')

            return secnum or tuple()

        def get_next_exercise_number(secnum):
            section = secnum[0]
            exercise_counter[section] = exercise_counter.get(section, 0) + 1
            return (section, exercise_counter[section],)

        def register_exercise_number(docname, secnum, exercise):
            env.toc_exercise_numbers.setdefault(docname, {})
            number = get_next_exercise_number(secnum)
            env.toc_exercise_numbers[docname][exercise.signature] = number
            env.toc_exercises[exercise.signature] = number

        def _walk_doctree(docname, doctree, secnum) -> None:
            for subnode in doctree.children:
                if isinstance(subnode, nodes.section):
                    next_secnum = get_section_number(docname, subnode)
                    if next_secnum:
                        _walk_doctree(docname, subnode, next_secnum)
                    else:
                        _walk_doctree(docname, subnode, secnum)
                elif isinstance(subnode, addnodes.toctree):
                    for title, subdocname in subnode['entries']:
                        if url_re.match(subdocname) or subdocname == 'self':
                            # don't mess with those
                            continue

                        _walk_doc(subdocname, secnum)
                elif isinstance(subnode, exercise):
                    register_exercise_number(docname, secnum, subnode)
                    _walk_doctree(docname, subnode, secnum)

                elif isinstance(subnode, nodes.Element):
                    _walk_doctree(docname, subnode, secnum)

        def _walk_doc(docname, secnum) -> None:
            if docname not in assigned:
                assigned.add(docname)
                doctree = env.get_doctree(docname)
                _walk_doctree(docname, doctree, secnum)

        _walk_doc(env.config.master_doc, tuple())
        for docname, exercise_number in env.toc_exercise_numbers.items():
            if exercise_number != old_exercise_numbers.get(docname):
                rewrite_needed.append(docname)

        return rewrite_needed

def setup(app):
    visitors = (visit_exercise, depart_exercise)

    app.add_config_value('hide_solutions', False, 'html')

    app.add_node(exercise, html=visitors, latex=visitors, text=visitors)
    app.add_node(solution, html=(visit_solution, depart_solution))

    app.add_directive('exercise', ExerciceDirective)
    app.add_directive('solution', SolutionDirective)

    app.add_env_collector(ExercisesCollector)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }