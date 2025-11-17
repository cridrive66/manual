# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Read the Docs Git LFS fix
import os
import sys

# Git LFS setup for Read the Docs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    print("=== READTHEDOCS GIT LFS SETUP ===")
    
    # Method 1: Use system Git LFS if available
    print("Method 1: Trying system Git LFS...")
    lfs_result = os.system('git lfs pull')
    
    if lfs_result != 0:
        # Method 2: Manual Git LFS binary download and setup
        print("Method 2: Downloading Git LFS binary...")
        os.system('wget -q https://github.com/git-lfs/git-lfs/releases/download/v3.5.1/git-lfs-linux-amd64-v3.5.1.tar.gz')
        os.system('tar -xzf git-lfs-linux-amd64-v3.5.1.tar.gz')
        os.system('cd git-lfs-3.5.1 && ./install.sh')
        os.system('git lfs pull')
        print("Git LFS binary setup complete")
    
    # Verify files were downloaded
    if os.path.exists('_static/video'):
        video_files = os.listdir('_static/video')
        print(f"Video directory contents: {video_files}")
    else:
        print("WARNING: _static/video directory not found!")
    
    print("=== GIT LFS SETUP COMPLETE ===")


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
html_extra_path = ['_static/video']

# Debug: Check if videos are accessible
if on_rtd:
    print("Checking video paths...")
    video_path = '_static/video/installation.mp4'
    if os.path.exists(video_path):
        print(f"✅ Video exists: {video_path}")
        print(f"Video size: {os.path.getsize(video_path)} bytes")
    else:
        print(f"❌ Video NOT found: {video_path}")
        print(f"Current directory: {os.getcwd()}")
        print(f"Directory contents: {os.listdir('.')}")