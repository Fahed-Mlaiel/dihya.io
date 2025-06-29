# test_utils_helper_advanced.py – Tests ultra avancés pour utils_helper.py (helpers/core)
from backend.components.metiers.restauration.utils.helpers.core.utils_helper import format_date, is_object, deep_clone
import pytest
from backend.components.metiers.restauration.utils.helpers.impl.advanced_impl_helper import validate_and_audit
from datetime import datetime

def test_validate_and_audit_core_valide():
    data = {'id': 10, 'user': 'CoreUser', 'email': 'core@example.com'}
    result = validate_and_audit(data)
    assert result['valid'] is True
    assert result['data']['user'] == 'anonyme'
    assert 'timestamp' in result['audit']

def test_validate_and_audit_core_invalide():
    result = validate_and_audit({})
    assert result['valid'] is False
    assert result['data'] == {}

def test_format_date_iso():
    d = datetime(2025, 6, 11, 12, 0, 0).isoformat()
    assert format_date(d) == '2025-06-11T12:00:00'

def test_is_object():
    assert is_object({'a': 1}) is True
    assert is_object([1, 2]) is False
    assert is_object(None) is False
    assert is_object('str') is False

def test_deep_clone():
    obj = {'a': 1, 'b': {'c': 2}}
    clone = deep_clone(obj)
    assert clone == obj
    assert clone is not obj
    clone['b']['c'] = 99
    assert obj['b']['c'] == 2

def test_deep_clone_empty():
    assert deep_clone({}) == {}

def test_format_date_type():
    d = datetime.now().isoformat()
    assert isinstance(format_date(d), str)
