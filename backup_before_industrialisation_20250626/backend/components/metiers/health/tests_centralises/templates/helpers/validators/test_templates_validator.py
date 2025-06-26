import pytest
from health.templates.helpers.validators.templates_validator import is_valid_template_file, validate_template_content
import tempfile
import os

def test_is_valid_template_file(tmp_path):
    # Fichier valide
    valid_file = tmp_path / "template.html.j2"
    valid_file.write_text("<div>{{ var }}</div>")
    assert is_valid_template_file(str(valid_file))
    # Fichier inexistant
    assert not is_valid_template_file(str(tmp_path / "notfound.html.j2"))
    # Extension invalide
    invalid_file = tmp_path / "invalid.exe"
    invalid_file.write_text("")
    assert not is_valid_template_file(str(invalid_file))

def test_validate_template_content():
    assert validate_template_content('<div>{{ var }}</div>')
    assert validate_template_content('{ "a": 1 }')
    assert not validate_template_content('no tags')
    assert not validate_template_content('')
    # Edge cases
    assert validate_template_content('{{}}')
    assert validate_template_content('<>')
    assert validate_template_content('{}')
