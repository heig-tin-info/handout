"""
Replace Pygments for writing highlighted code-block with
traditional LaTeX Listings environment.
"""
from docutils import nodes
from sphinx.util import logging
from sphinx.util.console import colorize
from sphinx.writers.latex import LaTeXTranslator
from types import SimpleNamespace
from sphinx.builders.latex.nodes import captioned_literal_block

supported_languages = [
    'ACSL', 'Ada', 'Ant', 'Algol', 'Assembler', 'Awk', 'C++', 'C', 'CIL',
    'Clean', 'Cobol', 'Comal', 'command.com', 'Comsol', 'csh', 'Delphi',
    'Eiffel, Elan', 'elisp', 'erlang', 'Euphoria, Fortran', 'GAP', 'GCL',
    'Gnuplot', 'Go', 'hansl', 'Haskell', 'HTML', 'IDL', 'inform', 'Java',
    'JVMIS', 'ksh', 'Lingo', 'Lisp', 'LLVM', 'Logo', 'Lua', 'make',
    'Mathematica', 'Matlab', 'Mercury', 'MetaPost', 'Miranda', 'Mizar',
    'ML', 'Modula-2', 'MuPAD', 'NASTRAN', 'Oberon-2', 'OCL', 'Octave',
    'OORexx', 'Oz', 'Pascal', 'Perl', 'PHP', 'PL/I', 'Plasm', 'PostScript',
    'POV', 'Prolog', 'Promela', 'PSTricks', 'Python', 'R', 'Reduce', 'Rexx',
    'RSL', 'Ruby', 'S', 'SAS', 'Scala', 'Scilab', 'sh', 'SHELXL', 'Simula',
    'SPARQL', 'SQL', 'Swift', 'tcl', 'TeX', 'VBScript', 'Verilog', 'VHDL',
    'VRML', 'XML', 'XSLT']

class MyLaTeXTranslator(LaTeXTranslator):
    def __init__(self, document, builder, theme = None):
        super().__init__(document, builder)
        self.supported_languages = [
            lang.lower().strip()
            for lang in supported_languages
        ]

    def visit_literal_block(self, node):
        if node.rawsource != node.astext():
            # most probably a parsed-literal block -- don't highlight
            self.in_parsed_literal += 1
            self.body.append('\\begin{sphinxalltt}\n')
        else:
            labels = self.hypertarget_to(node)
            if isinstance(node.parent, captioned_literal_block):
                labels += self.hypertarget_to(node.parent)
            if labels and not self.in_footnote:
                self.body.append('\n\\def\\sphinxLiteralBlockLabel{' + labels + '}')

            self.body.append('\n' + self.literal_block_listing(node) + '\n')
            raise nodes.SkipNode

    def language_name(self, name):
        return '' if not name in self.supported_languages else name

    def literal_block_listing(self, node):
        highlight_args = node.get('highlight_args', {})
        conf = SimpleNamespace(
            lang= node.get('language', ''),
            linenos= node.get('linenos', False),
            lineno_start= highlight_args.get('linenos-start', None),
            hl_lines= highlight_args.get('hl_lines', None)
        )

        # Into Listing language name
        conf.lang = self.language_name(conf.lang)

        # Process arguments
        env_settings = []
        env_settings.append(f'language={conf.lang}')
        if conf.linenos:
            env_settings.append('numbers=left')
        if conf.lineno_start:
            env_settings.append('firstnumber={conf.lineno_start}')
        if conf.hl_lines and len(conf.hl_lines) >= 2:
            env_settings.append('linerange=%d-%d' % tuple(conf.hl_lines))

        # Format code
        return ''.join([
            '\\begin{lstlisting}[%s]\n' % ','.join(env_settings),
            node.rawsource,
            '\n\\end{lstlisting}'
        ])

def setup(app):
    app.set_translator('latex', MyLaTeXTranslator)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
