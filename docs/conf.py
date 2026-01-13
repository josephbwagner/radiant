"""Sphinx configuration for Radiant documentation."""

project = "Radiant"
copyright = "2026, Joseph Wagner"
author = "Joseph Wagner"
version = "0.1.0"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/josephbwagner/radiant/",
    "source_branch": "main",
    "source_directory": "docs/",
}

html_static_path = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "fastapi": ("https://fastapi.tiangolo.com", None),
}

autodoc_typehints = "description"
autodoc_member_order = "bysource"
