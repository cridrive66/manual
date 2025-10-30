# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'APRIORA plugin manual'
copyright = '2025, Cristiano Guidi'
author = 'Cristiano Guidi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.video',
    'sphinx.ext.mathjax'
]

templates_path = ['_templates']
exclude_patterns = []
math_numfig = True # for equation numbering
numfig = True # for figure/table numbering


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_logo = 'images/icon.png'
html_static_path = ['_static']
html_css_files = ["css/custom.css"]
