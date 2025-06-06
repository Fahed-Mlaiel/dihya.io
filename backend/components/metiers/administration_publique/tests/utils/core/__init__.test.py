# __init__.test.py – Test d'import global du module core (Python)
from . import *

def test_import_core_utils():
    assert callable(generate_id)
    assert callable(deep_clone)
    assert callable(is_valid_email)
    assert callable(audit_log)
