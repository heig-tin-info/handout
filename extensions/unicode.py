"""
Create the role :unicode:`` to link to an unicode char. It will be
replaced to an hyperlink to the unicode-table website.
"""
import re
from docutils import nodes

def unicode_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    app = inliner.document.settings.env.app
    node = make_link_node(rawtext, text, app)
    return [node], []

def make_link_node(rawtext, text, app, **options):
    m = re.match('U\+([A-Fa-f0-9]{4})', text)
    if not m:
        raise ValueError('Wrong unicode format: %s', rawtext)

    ref = 'https://unicode-table.com/en/%s/' % m.groups()[0]
    return nodes.reference(rawtext, text, refuri=ref, **options)

def setup(app):
    app.add_role('unicode', unicode_role)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }