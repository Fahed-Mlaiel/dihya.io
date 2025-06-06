"""
Tests ultra avancés pour fixtures_generator.py (Python)
"""
from .fixtures_generator import generate_model, generate_user

def test_generate_model_ultra():
    model = generate_model('UltraModel', 12, 20)
    assert isinstance(model, dict)
    assert model['name'] == 'UltraModel'
    assert model['type'] == 'mesh'
    assert len(model['vertices']) == 12
    assert len(model['faces']) == 20
    assert model['meta']['generated'] is True

def test_generate_user_ultra():
    user = generate_user('superadmin')
    assert isinstance(user, dict)
    assert user['role'] == 'superadmin'
    assert user['name'].startswith('User_superadmin_')
