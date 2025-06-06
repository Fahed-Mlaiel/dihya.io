# templates_helper.test.py – Tests unitaires Python pour helpers templates Threed
import unittest
import pytest
from backend.components.metiers.threed.templates.helpers.templates_helper import render_template, is_valid_template, mock_template_context, TemplatesHelper

class TestTemplatesHelper(unittest.TestCase):
    def test_render_template(self):
        self.assertTrue(callable(render_template))
    def test_is_valid_template(self):
        self.assertTrue(is_valid_template('rapport_audit.html.j2'))
        self.assertTrue(is_valid_template('foo.txt'))
        self.assertFalse(is_valid_template('foo.exe'))
    def test_mock_template_context(self):
        self.assertIsInstance(mock_template_context(), dict)

def test_templates_helper_init():
    helper = TemplatesHelper(options={"mode": "test"})
    assert helper.options == {"mode": "test"}
    assert helper.get_audit_trail() == []

def test_templates_helper_config_and_audit():
    helper = TemplatesHelper()
    assert helper.init({"version": 1}) is True
    assert helper.config == {"version": 1}
    assert helper.get_audit_trail()[0]["action"] == 'init'

def test_templates_helper_assist_valid():
    helper = TemplatesHelper()
    helper.init({"version": 2})
    result = helper.assist("OP", {"foo": "bar"})
    assert result == {"success": True, "operation": "OP", "data": {"foo": "bar"}, "config": {"version": 2}}
    assert len(helper.get_audit_trail()) == 2
    assert helper.get_audit_trail()[1]["action"] == 'assist'

def test_templates_helper_assist_invalid():
    helper = TemplatesHelper()
    with pytest.raises(ValueError):
        helper.assist(None, {})
    assert helper.get_audit_trail()[0]["action"] == 'error'

if __name__ == '__main__':
    unittest.main()
