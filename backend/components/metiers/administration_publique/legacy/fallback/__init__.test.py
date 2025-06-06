from . import samples

def test_import_samples():
    assert samples is not None
    assert hasattr(samples, 'sample_fallback_legacy')
