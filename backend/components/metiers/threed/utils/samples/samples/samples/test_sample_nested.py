# Test unitaire pour sample_nested.py
def test_get_nested_sample():
    from .sample_nested import get_nested_sample
    sample = get_nested_sample()
    assert sample["valid"] is True
    assert sample["level"] == 3
