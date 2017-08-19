#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))
from td1a_unit_test_ci import __version__

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'td1a_unit_test_ci'
copyright = '2017, Xavier Dupré'
author = 'Xavier Dupré'
version = __version__
release = __version__
language = 'fr'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {}
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}

htmlhelp_basename = 'td1a_unit_test_cidoc'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc,
     'td1a_unit_test_ci.tex',
     'td1a\\_unit\\_test\\_ci Documentation',
     'Xavier Dupré',
     'manual'),
]

texinfo_documents = [
    (master_doc, 'td1a_unit_test_ci', 'td1a_unit_test_ci Documentation',
     author, 'td1a_unit_test_ci', 'One line description of project.',
     'Miscellaneous'),
]

intersphinx_mapping = {'https://docs.python.org/': None}
