# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config
import os
import sys

sys.path.append(os.path.abspath("./_ext"))

project = 'Introduction au C'
author = 'Pierre Bressy, Didier Mettler, François Birling, Yves Chevallier'
copyright = 'HEIG-VD(c) 2019'

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'exercices',
    'span-sectnum'
]

source_suffix = ['.rst']

templates_path = ['_templates']

language = 'fr'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'heigvd'

latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'babel': '\\usepackage{polyglossia}\n\\setmainlanguage{fr}'
}

numfig = True
#highlight_language = 'c'

html_secnumber_suffix = '  '
