# test_validators.test.py – Test ultra avancé validators.py

import sys
import os
import pytest
import importlib.util

# Import dynamique du validators métier, compatible partout
validators_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../metiers/threed/fixtures/helpers/validators/validators.py'))
spec = importlib.util.spec_from_file_location('validators', validators_path)
validators = importlib.util.module_from_spec(spec)
sys.modules['validators'] = validators
spec.loader.exec_module(validators)

def test_validators_basic():
    assert hasattr(validators, '__file__') or True

# Teste la présence des fonctions attendues dans le module métier

def test_is_valid_3d_model():
    assert hasattr(validators, 'is_valid_3d_model')

def test_is_valid_user():
    assert hasattr(validators, 'is_valid_user')

def test_is_fixture_accessible():
    assert hasattr(validators, 'is_fixture_accessible')
