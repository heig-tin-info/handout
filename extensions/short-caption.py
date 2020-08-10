import sphinx
from docutils import nodes
from sphinx.directives import SphinxDirective
from sphinx.writers.latex import LaTeXTranslator
from sphinx.builders.latex.nodes import captioned_literal_block
from sphinx.util import logging, texescape

logger = logging.getLogger(__name__)


def visit_caption(self, node):
    self.in_caption += 1
    if isinstance(node.parent, captioned_literal_block):
        self.body.append('\\sphinxSetupCaptionForVerbatim{')
    elif self.in_minipage and isinstance(node.parent, nodes.figure):
        self.body.append('\\captionof{figure}{')
    elif self.table and node.parent.tagname == 'figure':
        self.body.append('\\sphinxfigcaption{')
    else:
        # Use alt text as short caption for the \listoffigures
        short = ''
        if isinstance(node.parent, nodes.figure):
            if isinstance(node.parent.children[0], nodes.image):
                alt = node.parent.children[0].get('alt')
                if alt:
                    short = '[' + texescape.escape(alt) + ']'
        self.body.append('\\caption%s{' % short)


def setup(app):
    LaTeXTranslator.visit_caption = visit_caption

    major, minor, patch = tuple(map(int, sphinx.__version__.split('.')))
    if major > 3 or (major == 3 and minor > 3):
        logger.warn('Check if PR #8089 was merged')

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
