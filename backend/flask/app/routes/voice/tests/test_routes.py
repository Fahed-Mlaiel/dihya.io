import pytest
from ..services import get_voice_data, create_voice_entry, update_voice_entry, delete_voice_entry, search_voice

def test_create_voice_entry():
    data = {"name": "Voix IA", "lang": "fr"}
    result = create_voice_entry(data, user="testuser")
    assert result["status"] == "created"

def test_get_voice_data():
    result = get_voice_data(1, user="testuser")
    assert "id" in result

def test_update_voice_entry():
    data = {"name": "Voix IA Premium", "lang": "fr"}
    result = update_voice_entry(1, data, user="testuser")
    assert result["status"] == "updated"

def test_delete_voice_entry():
    result = delete_voice_entry(1, user="testuser")
    assert result["status"] == "deleted"

def test_search_voice():
    result = search_voice({"query": "voix"}, user="testuser")
    assert isinstance(result, list)
