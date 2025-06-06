"""
Test unitaire pour sample_validator.py
"""
from .sample_validator import sample_validator_usage
def test_sample_validator_usage():
    assert sample_validator_usage() == 'sample validator usage'
