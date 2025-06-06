# exporter_helper.test.py
# Tests unitaires Python pour exporter_helper
from .exporter_helper import format_export_json

def test_format_export_json():
    obj = {'a': 1, 'b': 'x'}
    assert format_export_json(obj) == '{"a": 1, "b": "x"}' or format_export_json(obj) == '{"b": "x", "a": 1}'
