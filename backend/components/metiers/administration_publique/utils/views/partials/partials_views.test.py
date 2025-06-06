"""
partials_views.test.py – Tests unitaires partials views threed (Python)
"""
from .partials_views import render_widget

def test_render_widget():
    html = render_widget('badge', 'OK')
    assert "widget-badge" in html
    assert ">OK<" in html
