# logger_helper.test.py
# Tests unitaires Python pour logger_helper
from .logger_helper import format_log
import re

def test_format_log():
    result = format_log('info', 'Test')
    assert re.match(r'\[INFO\]\[.*\] Test', result)
