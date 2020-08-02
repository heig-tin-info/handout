# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config
import os
import sys
import subprocess

sys.path.append(os.path.abspath("./_ext"))

project = 'Le C pour l\'ingenieur'
author = 'Prof. Yves Chevallier'
copyright = 'HEIG-VD(c) 2019'
release = subprocess.check_output(["git", "describe"]).strip().decode('utf8')

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
#    'sphinxcontrib.bibtex',
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
smartquotes = False

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_static_path = ['_static']

html_theme = 'heigvd'
html_secnumber_suffix = '  '
html_last_updated_fmt = r'%d %b %Y (version ' + release + ')'
html_css_files = [
    'custom.css'
]

numfig = True

pygments_style = "colorful"

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
    'pointsize': '12pt',
    'babel': r'\usepackage[french]{babel}',
    'inputenc': '',
    'utf8extra': '',
    'fontpkg': '',
    'fncychap': '',
    'printindex': '',
    'maketitle': r'\maketitle',
    'preamble': r'''

% Disable the ugly colouring of titles. Why does Sphinx do this?
\definecolor{TitleColor}{rgb}{0,0,0}
\definecolor{InnerLinkColor}{rgb}{0,0,0}

\usepackage{fontspec}
\setmonofont{DejaVu Sans Mono}

\usepackage{colortbl}
\usepackage{xcolor,graphicx}
\usepackage[xparse,skins,breakable]{tcolorbox}

\newtcolorbox{hint}{breakable,enhanced,arc=0mm,colback=lightgray!5,colframe=lightgray,leftrule=11mm,%
height from=1.3cm to 16cm,%
overlay={\node[anchor=north west,outer sep=1mm] at (frame.north west) {
    \includegraphics[width=2em]{../../icons/hint.pdf}}; }}

\renewenvironment{sphinxnote}[1]
    {\begin{hint}{#1}}
    {\end{hint}}

% Change code-block style
\colorlet{aaa}{lightgray}
\colorlet{foobar}{lightgray!8}
\sphinxsetup{%
  VerbatimColor={named}{foobar},
  verbatimwithframe=true,
  VerbatimBorderColor={named}{aaa},
  verbatimborder=0.3mm,
  OuterLinkColor={rgb}{0.55,0.06,0.09}
}

% Define header and footers
\makeatletter
\fancypagestyle{normal}{
  \fancyhf{}
  \fancyfoot{}
  \fancyhead{}
  \fancyhead[LE,RO]{{\thepage}}
  \fancyhead[CO]{\uppercase{Le C pour l'ingénieur}}
  \fancyhead[CE]{\leftmark}
  \renewcommand{\headrulewidth}{0.2pt}
  \renewcommand{\footrulewidth}{0pt}
}
\makeatother

'''
}

latex_logo = '_artifacts/heig-vd.pdf'

man_pages = [
    ('index', 'info', None, author, 1)
]
