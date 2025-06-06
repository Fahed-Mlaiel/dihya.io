"""
Test unitaire pour sample_view.py
"""
from .sample_view import render
def test_render():
    assert render() == '<div>Vue 3D</div>'
