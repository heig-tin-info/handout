import os
import sys
sys.path.append(os.path.abspath("../extensions"))

project = "Le C pour l'ingénieur"
copyright = '2023, HEIG-VD'
author = 'Prof. Yves Chevallier'

extensions = [
    "myst_parser",
    "sphinx_exercise",
    "sphinx_togglebutton",
    "sphinx.ext.mathjax",
    'sphinx_copybutton',
    "sphinx_design",
    "sphinx_prompt",
    "sphinx_tippy",
    "sphinx.ext.todo",
    "unicode",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

master_doc = "index"

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_logo = "_static/2020-slim.svg"
html_title = "Le C pour l'ingénieur"

html_theme_options = {
    "logo": {
        "image_light": "_static/2020-slim.svg",
        "image_dark": "_static/2020-slim-white.svg",
        "text": "Le C pour l'ingénieur",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/heig-tin-info/handout",
            "icon": "fa-brands fa-github",
        },
    ],
    "header_links_before_dropdown": 4,
    "show_nav_level": 2,
    "show_toc_level": 1,
    "navigation_depth": 2,
    "collapse_navigation": True,
    "navbar_align": "left",
    "pygment_dark_style": "lightbulb",
}
html_context = {
    "github_user": "heig-tin-info",
    "github_repo": "handout",
    "github_version": "master",
}

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "strikethrough",
    "substitution",
    "tasklist"
]

latex_engine = "xelatex"

# tippy_props = {"placement": "auto-start", "maxWidth": 500, "interactive": False, "arrow": True}
tippy_add_class = "has-tippy"

html_static_path = ['_static']
html_css_files = [
    "css/custom.css",
    "css/tippy.css"
]
