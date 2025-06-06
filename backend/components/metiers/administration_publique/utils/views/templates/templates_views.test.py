"""
templates_views.test.py – Tests unitaires templates views threed (Python)
"""
from .templates_views import render_template

def test_render_template():
    html = render_template('page', 'Hello')
    assert "template-page" in html
    assert ">Hello<" in html
