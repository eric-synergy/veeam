# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Veeam'
copyright = str(date.today().year) + ", Eric W. All rights reserved."
author = 'Eric W'

release = '1.0'
version = '1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinxemoji.sphinxemoji", 
    "sphinx_contributors", 
    "sphinx_copybutton"
]

sphinxemoji_style = 'twemoji'

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
# intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

exclude_patterns = []
# -- Options for HTML output

html_title = "V Demo"
html_theme_options = {}
html_theme_options["announcement"] = (
        " Welcome to V Lab "

)

#html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for EPUB output

