# views.test.py
"""Tests unitaires Python pour core views"""
from .views import render_core_view

def test_render_core_view():
    assert 'Test' in render_core_view('Test')
