# Configuration file for the Sphinx documentation builder.

import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath('../../src'))

# Project information
project = '{{ cookiecutter.project_name }}'
copyright = '{% now "utc", "%Y" %} {{ cookiecutter.author_name }}'
author = '{{ cookiecutter.author_name }}'
release = '{{ cookiecutter.first_version }}'

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
