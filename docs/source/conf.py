# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rtd-tutorial-ybeen'
copyright = '2023, ybeen'
author = 'ybeen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



extensions = ['myst_nb']
source_suffix = ['.rst', '.md', '.ipynb']



templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # in conf.py file
html_static_path = ['_static']


# LaTex UNICODE Options --------------------------------
latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
    \setmainfont{DejaVu Serif}
    \setsansfont{DejaVu Sans}
    \setmonofont{DejaVu Sans Mono}
    ''',
    'inputenc': '',
    'utf8extra': '',
}

