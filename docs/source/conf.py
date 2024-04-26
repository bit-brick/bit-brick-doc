# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sys
import os
import shlex

import sphinx_rtd_theme
import recommonmark

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('.'))

source_suffix = ['.rst', '.md']

# -- Project information -----------------------------------------------------

project = "Bit-Brick"
copyright = '2024, Bit-Brick'
author = 'Bit-Brick'

# The full version, including alpha/beta/rc tags
release = ""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'recommonmark',
    'sphinx_markdown_tables',
]

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

version = recommonmark.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = []
exclude_patterns = ['_build']

default_role = None

pygments_style = 'sphinx'

todo_include_todos = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = "sphinx_material"
html_theme = "sphinx_book_theme"
# html_theme = "furo"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

htmlhelp_basename = 'Recommonmarkdoc'

latex_elements = {

}

latex_documents = [
  (master_doc, 'Recommonmark.tex', u'Recommonmark Documentation',
   u'Lu Zero, Eric Holscher, and contributors', 'manual'),
]

man_pages = [
    (master_doc, 'recommonmark', u'Recommonmark Documentation',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'Recommonmark', u'Recommonmark Documentation',
   author, 'Recommonmark', 'One line description of project.',
   'Miscellaneous'),
]


def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_math': False,
        'enable_inline_math': False,
        'enable_eval_rst': True,
        'enable_auto_doc_ref': True,
    }, True)
    app.add_transform(AutoStructify)

