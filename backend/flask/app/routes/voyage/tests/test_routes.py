import pytest
from ..services import get_voyage_data, create_voyage_entry, update_voyage_entry, delete_voyage_entry, search_voyage

def test_create_voyage_entry():
    data = {"destination": "Paris", "date": "2025-06-01"}
    result = create_voyage_entry(data, user="testuser")
    assert result["status"] == "created"

def test_get_voyage_data():
    result = get_voyage_data(1, user="testuser")
    assert "id" in result

def test_update_voyage_entry():
    data = {"destination": "Lyon", "date": "2025-06-02"}
    result = update_voyage_entry(1, data, user="testuser")
    assert result["status"] == "updated"

def test_delete_voyage_entry():
    result = delete_voyage_entry(1, user="testuser")
    assert result["status"] == "deleted"

def test_search_voyage():
    result = search_voyage({"query": "Paris"}, user="testuser")
    assert isinstance(result, list)
