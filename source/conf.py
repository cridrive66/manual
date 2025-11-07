# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Read the Docs Git LFS fix
# import os
# if os.environ.get('READTHEDOCS') == 'True':
#     # Install and set up Git LFS on Read the Docs
#     os.system("curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash")
#     os.system("sudo apt-get install git-lfs")
#     os.system("git lfs install")
#     os.system("git lfs pull")

# Read the Docs Git LFS fix
import os
import subprocess

if os.environ.get('READTHEDOCS') == 'True':
    print("Setting up Git LFS on Read the Docs...")
    # Install Git LFS
    subprocess.run(['wget', 'https://github.com/git-lfs/git-lfs/releases/download/v3.5.1/git-lfs-linux-amd64-v3.5.1.tar.gz'])
    subprocess.run(['tar', 'xvfz', 'git-lfs-linux-amd64-v3.5.1.tar.gz'])
    subprocess.run(['./git-lfs', 'install'])
    subprocess.run(['./git-lfs', 'pull'])
    print("Git LFS setup complete")

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
