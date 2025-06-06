"""
Test unitaire pour sample_core_helper.py
"""
from .sample_core_helper import sample_core_usage
def test_sample_core_usage():
    assert sample_core_usage() == 'sample core usage'
