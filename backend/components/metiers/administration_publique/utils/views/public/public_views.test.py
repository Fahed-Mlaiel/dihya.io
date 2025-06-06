# public_views.test.py
"""Tests unitaires Python pour public_views"""
from .public_views import render_public_info

def test_render_public_info():
    assert 'Bienvenue' in render_public_info('Bienvenue')
