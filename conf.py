# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config
import os
import sys

sys.path.append(os.path.abspath("./_ext"))

project = "Le C pour l'ingénieur"
author = 'Pierre Bressy, Didier Mettler, François Birling, Yves Chevallier'
copyright = 'HEIG-VD(c) 2019'

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinxcontrib.rsvgconverter',
    'exercices',
    'unicode',
    'appendix',
    'span-sectnum'
]

source_suffix = ['.rst']

templates_path = ['_templates']

language = 'fr'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'heigvd'
html_secnumber_suffix = '  '

numfig = True

latex_additional_files = [
    '_templates/manual.cls',
    '_templates/sphinx.sty',
    '_templates/latexmkrc'
]

latex_documents = [
    ('index', 'main.tex', None , 'Prof. Yves Chevallier' , 'manual')
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
