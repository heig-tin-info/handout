import re

from sphinx.writers.latex import LaTeXTranslator
from sphinx.writers.html5 import HTML5Translator

from sphinx import addnodes
from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import Directive, directives

latex_preamble = r"""
\newcounter{multicolminlines}
\setcounter{multicolminlines}{1}

\makeatletter
\xpatchcmd\balance@columns
   {\ifnum\dimen@<\topskip
     \mult@info\@ne
       {Start value
          \the\dimen@  \space ->
          \the\topskip \space (corrected)}%
     \dimen@\topskip
   \fi}
   {\skip@\c@multicolminlines\baselineskip
   \advance\skip@-\baselineskip
   \advance\skip@\topskip
   \ifnum\dimen@<\skip@
     \mult@info\@ne
       {Start value
          \the\dimen@  \space ->
          \the\skip@ \space (corrected)}%
     \dimen@\skip@
   \fi
   }
   {\typeout{Success!}}{\patchFAILED}

\define@key{hlist@keys}{columns}{\def\hlist@columns{#1}}%
\define@key{hlist@keys}{minlines}{\def\hlist@minlines{#1}}%

\newcommand{\fixspacing}{\vspace{0pt plus 1filll}\mbox{}}

\newenvironment{hlist}[1][]{%
    \setkeys{hlist@keys}{columns=4,minlines=4,#1}
    \setcounter{multicolminlines}{\hlist@minlines}
    \begin{multicols}{\hlist@columns}

}{

    \fixspacing
    \end{multicols}
}
\makeatother
"""

def visit_latex_hlist(self, node):
    options = [
        f'columns={node["columns"]}' if node['columns'] else '',
        f'min-lines={node["min-lines"]}' if node['min-lines'] else ''
    ]
    self.body.append('\\begin{hlist}[%s]\n' % ','.join(options))
    if self.table:
        self.table.has_problematic = True


def depart_latex_hlist(self, node):
    self.body.append('\\end{hlist}\n')


def visit_html_hlist(self, node):
    cols = node['columns']
    self.body.append((
        f'<div style="-webkit-column-count: {cols};'
        f'-moz-column-count: {cols}; column-count: {cols};">'
    ))


def depart_html_hlist(self, node):
    self.body.append('</div>\n')


class HList(SphinxDirective):
    """
    Directive for a list that gets compacted horizontally.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'columns': int,
        'max-height': int,
    }

    def run(self):
        hlist = addnodes.hlist()
        hlist['columns'] = self.options.get('columns', None)
        hlist['min-lines'] = self.options.get('min-lines', None)
        hlist.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, hlist)

        if len(hlist.children) != 1 or not isinstance(hlist.children[0],
                                                      (nodes.bullet_list, nodes.enumerated_list)):
            reporter = self.state.document.reporter
            return [reporter.warning('.. hlist content is not a list', line=self.lineno)]

        return [hlist]


def add_latex_environment(app):
    if hasattr(app.builder, 'context'):
        context = app.builder.context
        context['preamble'] += latex_preamble


def setup(app):
    LaTeXTranslator.visit_hlist = visit_latex_hlist
    LaTeXTranslator.depart_hlist = depart_latex_hlist

    HTML5Translator.visit_hlist = visit_html_hlist
    HTML5Translator.depart_hlist = depart_html_hlist

    app.connect('builder-inited', add_latex_environment)

    app.add_directive('hlist', HList, override=True)

    app.add_latex_package('multicol', 'balancingshow')
    app.add_latex_package('regexpatch')
    app.add_latex_package('keyval')

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
