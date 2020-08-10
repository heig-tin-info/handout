# Configuration file for the Sphinx documentation builder.
import os
import sys
import subprocess
import datetime

now = datetime.datetime.now()
sys.path.append(os.path.abspath("./extensions"))

project = 'Le C pour l\'ingenieur'
author = 'Prof. Yves Chevallier'
copyright = f'HEIG-VD(c) {now.year}'
release = subprocess.check_output(["git", "describe"]).strip().decode('utf8')

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
#    'sphinxcontrib.bibtex',
    'sphinxcontrib.rsvgconverter',
    'listings',
    'exercises',
    'unicode',
    'appendix',
    'gtag',
    'hlist',
    'span-sectnum'
]

googleanalytics_id = 'UA-145664552-1'

source_suffix = ['.rst']

templates_path = ['assets/templates']

language = 'fr'
smartquotes = False

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'summary/*.rst']

html_theme = 'heigvd'
html_secnumber_suffix = '  '
html_last_updated_fmt = r'%d %b %Y (version ' + release + ')'

numfig = True

pygments_style = "colorful"

latex_additional_files = [
    'assets/templates/sphinx.sty',
    'assets/templates/footnotehyper-sphinx.sty'
]

latex_docclass = {
    'manual': 'book'
}

latex_documents = [
    ('index', 'main.tex', None , author, 'manual')
]

latex_use_xindy = False

latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'babel': r'\usepackage[french]{babel}',
    'inputenc': '',
    'utf8extra': '',
    'fontpkg': '',
    'fncychap': '',
    'printindex': '',
    'maketitle': r'\maketitle',
    'preamble': open('assets/templates/preamble.tex').read()
}

latex_logo = 'assets/images/heig-vd-small.pdf'

man_pages = [
    ('index', 'info', None, author, 1)
]
