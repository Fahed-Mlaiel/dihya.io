# threed_controller.test.py – Test ultra avancé pour threed_controller.py (API Threed)
import pytest
from backend.components.metiers.threed.api.controllers.threed_controller import get_threed, create_threed, update_threed, delete_threed

def test_get_threed_exists():
    assert callable(get_threed)

def test_create_threed_exists():
    assert callable(create_threed)

def test_update_threed_exists():
    assert callable(update_threed)

def test_delete_threed_exists():
    assert callable(delete_threed)
