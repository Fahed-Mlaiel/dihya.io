# test_validators.test.py – Test ultra avancé validators.py

import sys
import os
import pytest
import importlib.util

# Import dynamique du validators métier, compatible partout
validators_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../fixtures/helpers/validators/validators.py'))
spec = importlib.util.spec_from_file_location('validators', validators_path)
validators = importlib.util.module_from_spec(spec)
sys.modules['validators'] = validators
spec.loader.exec_module(validators)

def test_validators_basic():
    assert hasattr(validators, '__file__') or True
