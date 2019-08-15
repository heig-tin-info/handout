from docutils import nodes
from sphinx.writers.html5 import HTML5Translator

class Translator(HTML5Translator):
    def get_secnumber(self, node):
        # type: (nodes.Element) -> None
        if node.get('secnumber'):
            return node['secnumber']
        elif isinstance(node.parent, nodes.section):
            if self.builder.name == 'singlehtml':
                docname = self.docnames[-1]
                anchorname = "%s/#%s" % (docname, node.parent['ids'][0])
                if anchorname not in self.builder.secnumbers:
                    anchorname = "%s/" % docname  # try first heading which has no anchor
            else:
                anchorname = '#' + node.parent['ids'][0]
                if anchorname not in self.builder.secnumbers:
                    anchorname = ''  # try first heading which has no anchor
            if self.builder.secnumbers.get(anchorname):
                return self.builder.secnumbers[anchorname]
        return None

    def add_secnumber(self, node):
        secnumber = self.get_secnumber(node)
        if secnumber:
            self.body.append('<span class="sectnum">' + '.'.join(map(str, secnumber)) + '</span>')

def setup(app):
    #app.set_translator('html', Translator)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }