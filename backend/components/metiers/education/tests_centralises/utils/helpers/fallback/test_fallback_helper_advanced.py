# test_fallback_helper_advanced.py – Tests ultra avancés pour fallback.py (helpers/fallback)
import pytest
from backend.components.metiers.education.utils.logger.fallback.fallback import logger_fallback
from backend.components.metiers.education.utils.helpers.fallback.fallback import fallback_helper

def test_logger_fallback_auditabilite():
    log = logger_fallback('Fallback test')
    assert 'timestamp' in log
    assert log['message'] == 'Fallback test'

def test_logger_fallback_vide():
    log = logger_fallback('')
    assert 'timestamp' in log
    assert log['message'] == ''

def test_fallback_helper_success():
    assert fallback_helper(lambda: 42, 0) == 42

def test_fallback_helper_default():
    assert fallback_helper(lambda: (_ for _ in ()).throw(Exception('fail')), 'defaut') == 'defaut'

def test_fallback_helper_null():
    assert fallback_helper(lambda: None, 'x') is None

def test_fallback_helper_type():
    assert isinstance(fallback_helper(lambda: 'ok', 'ko'), str)
