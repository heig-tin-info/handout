"""Monkey patch literal block to show the real node location."""
from docutils import nodes
from docutils.nodes import Element
from sphinx.writers.html5 import HTML5Translator


def visit_literal_block(self, node: Element) -> None:
    if node.rawsource != node.astext():
        # most probably a parsed-literal block -- don't highlight
        return super().visit_literal_block(node)

    lang = node.get('language', 'default')
    linenos = node.get('linenos', False)
    highlight_args = node.get('highlight_args', {})
    highlight_args['force'] = node.get('force', False)
    if lang is self.builder.config.highlight_language:
        # only pass highlighter options for original language
        opts = self.builder.config.highlight_options
    else:
        opts = {}

    if linenos and self.builder.config.html_codeblock_linenos_style:
        linenos = self.builder.config.html_codeblock_linenos_style

    highlighted = self.highlighter.highlight_block(
        node.rawsource, lang, opts=opts, linenos=linenos,
        location=(node.source, node.line), **highlight_args
    )
    starttag = self.starttag(node, 'div', suffix='',
                             CLASS='highlight-%s notranslate' % lang)
    self.body.append(starttag + highlighted + '</div>\n')
    raise nodes.SkipNode


def setup(app):
    HTML5Translator.visit_literal_block = visit_literal_block

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
