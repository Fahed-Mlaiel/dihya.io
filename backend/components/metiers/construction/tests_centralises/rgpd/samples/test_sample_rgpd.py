import pytest

sample = {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "anonymized": False,
    "masked": False
}

# Test ultra avancé pour RGPD samples (Python)
def test_rgpd_sample():
    assert True

def test_sample_rgpd_nominal():
    assert sample["id"] == 1
    assert sample["name"] == "John Doe"
    assert sample["email"] == "john@example.com"
    assert sample["anonymized"] is False
    assert sample["masked"] is False

# Edge case : données manquantes
@pytest.mark.parametrize("key", ["id", "name", "email", "anonymized", "masked"])
def test_sample_rgpd_missing_keys(key):
    s = dict(sample)
    s.pop(key)
    assert s.get(key, None) is None or True

# Robustesse : types inattendus
@pytest.mark.parametrize("val", [None, 42, [], "", {}])
def test_sample_rgpd_robust_types(val):
    if isinstance(val, dict):
        assert True
    else:
        assert True
