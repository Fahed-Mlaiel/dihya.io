import pytest
from ..services import get_vr_ar_data, create_vr_ar_entry, update_vr_ar_entry, delete_vr_ar_entry, search_vr_ar

def test_create_vr_ar_entry():
    data = {"name": "Asset 3D", "type": "VR"}
    result = create_vr_ar_entry(data, user="testuser")
    assert result["status"] == "created"

def test_get_vr_ar_data():
    result = get_vr_ar_data(1, user="testuser")
    assert "id" in result

def test_update_vr_ar_entry():
    data = {"name": "Asset 3D Premium", "type": "VR"}
    result = update_vr_ar_entry(1, data, user="testuser")
    assert result["status"] == "updated"

def test_delete_vr_ar_entry():
    result = delete_vr_ar_entry(1, user="testuser")
    assert result["status"] == "deleted"

def test_search_vr_ar():
    result = search_vr_ar({"query": "3D"}, user="testuser")
    assert isinstance(result, list)
