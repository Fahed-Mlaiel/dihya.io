import pytest
from ..services import generate_uuid, sanitize_input, get_current_timestamp, log_event_util
from ..validators import is_valid_uuid, is_sanitized

def test_generate_uuid():
    uuid = generate_uuid()
    assert is_valid_uuid(uuid)

def test_sanitize_input():
    data = "<script>alert('xss')</script>"
    sanitized = sanitize_input(data)
    assert is_sanitized(sanitized)

def test_get_current_timestamp():
    ts = get_current_timestamp()
    assert "T" in ts

def test_log_event_util():
    assert log_event_util("test_event", user="testuser")
