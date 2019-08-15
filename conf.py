# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config
import os
import sys
import subprocess

sys.path.append(os.path.abspath("./_ext"))

project = "Le C pour l'ingénieur"
author = 'Prof. Yves Chevallier'
copyright = 'HEIG-VD(c) 2019'
release = subprocess.check_output(["git", "describe"]).strip().decode('utf8')

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinxcontrib.rsvgconverter',
    'exercices',
    'unicode',
    'appendix',
    'gtag',
    'span-sectnum'
]

googleanalytics_id = 'UA-145664552-1'

source_suffix = ['.rst']

templates_path = ['_templates']

language = 'fr'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'heigvd'
html_secnumber_suffix = '  '
html_last_updated_fmt = r'%d %b %Y (version ' + release + ')'

numfig = True

latex_additional_files = [
    '_templates/manual.cls',
    '_templates/sphinx.sty',
    '_templates/latexmkrc'
]

latex_documents = [
    ('index', 'main.tex', None , author, 'manual')
]

latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'babel': '\\usepackage[french]{babel}',
    'fontpkg': '',
    'fncychap': '',
    'preamble': '''
        % Disable the ugly colouring of titles. Why does Sphinx do this?
        \\definecolor{TitleColor}{rgb}{0,0,0}
        \\definecolor{InnerLinkColor}{rgb}{0,0,0}

    '''
}

latex_logo = '_artifacts/heig-vd.pdf'


man_pages = [
    ('index', 'info', None, author, 1)
]