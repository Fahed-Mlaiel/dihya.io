# threed_views.test.py
"""Tests unitaires Python pour threed_views"""
from .threed_views import render_3d

def test_render_3d():
    assert 'Cube' in render_3d('Cube')
