import json
import os

def test_rbac_data_admin():
    with open(os.path.join(os.path.dirname(__file__), 'sample_rbac_data.json')) as f:
        data = json.load(f)
    assert 'admin' in data['roles']
