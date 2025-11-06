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
    'sphinxcontrib.video',  # remove since I will upload every video with .. raw:: html
    'sphinx.ext.mathjax'
]

templates_path = ['_templates']
exclude_patterns = []
math_numfig = True # for equation numbering
numfig = True # for figure/table numbering


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/icon.png'
html_theme_options = {
    'logo_only': True,
}

html_static_path = ['_static']
html_css_files = ["css/custom.css"]
