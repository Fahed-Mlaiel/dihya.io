# __init__.test.py – Test d'import du point d'entrée users (fixtures/core/samples)
from . import sample_users

def test_import():
    assert hasattr(sample_users, 'sample_users_ultra')
