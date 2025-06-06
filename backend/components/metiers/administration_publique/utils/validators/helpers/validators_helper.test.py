# validators_helper.test.py
# Tests unitaires Python pour validators_helper
from .validators_helper import is_valid_email

def test_is_valid_email():
    assert is_valid_email('test@example.com')
    assert not is_valid_email('test@.com')
    assert not is_valid_email('test.com')
