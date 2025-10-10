# Configuration file for the Sphinx documentation builder.

import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath('../../src'))

# Project information
project = 'My enterprise Project'
copyright = '2025 Your Name'
author = 'Your Name'
release = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output options
html_theme = 'alabaster'
html_static_path = ['_static']
