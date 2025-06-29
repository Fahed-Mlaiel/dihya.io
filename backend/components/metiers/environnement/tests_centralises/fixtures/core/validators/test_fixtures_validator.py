# fixtures_validator.test.py – Test ultra avancé fixtures_validator.py
from environnement.fixtures.core.validators.fixtures_validator import (
    is_valid_environnement_model,
    is_valid_user,
)
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../../../../")
    ),
)


def test___init__():
    assert callable(is_valid_environnement_model)
    assert callable(is_valid_user)


def test___init___basic():
    assert is_valid_environnement_model({"id": "abc", "vertices": [], "faces": 0}) is True
    assert is_valid_user({"id": "u1", "role": "admin"}) is True
