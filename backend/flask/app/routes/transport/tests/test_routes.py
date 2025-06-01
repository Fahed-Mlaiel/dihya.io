import pytest
from ..services import get_transport_data, create_transport_entry, update_transport_entry, delete_transport_entry, search_transport

def test_create_transport_entry():
    data = {"name": "Bus", "capacity": 50}
    result = create_transport_entry(data, user="testuser")
    assert result["status"] == "created"

def test_get_transport_data():
    result = get_transport_data(1, user="testuser")
    assert "id" in result

def test_update_transport_entry():
    data = {"name": "Bus Express", "capacity": 60}
    result = update_transport_entry(1, data, user="testuser")
    assert result["status"] == "updated"

def test_delete_transport_entry():
    result = delete_transport_entry(1, user="testuser")
    assert result["status"] == "deleted"

def test_search_transport():
    result = search_transport({"query": "bus"}, user="testuser")
    assert isinstance(result, list)
