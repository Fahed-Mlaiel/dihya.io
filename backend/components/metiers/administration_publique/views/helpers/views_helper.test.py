"""Test unitaire pour views_helper.py"""
import importlib
import pytest

def test_render_helper_view_existe():
    mod = importlib.import_module('backend.components.metiers.threed.views.helpers.views_helper')
    assert hasattr(mod, 'render_helper_view')
    assert callable(getattr(mod, 'render_helper_view'))
# Ajouter d'autres tests unitaires selon les helpers disponibles
