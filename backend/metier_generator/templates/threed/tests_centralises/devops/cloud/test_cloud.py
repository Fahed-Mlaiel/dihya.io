"""
Tests avancés pour la gestion du cloud métier (provisioning, monitoring, sécurité, etc.).
"""
import importlib.util
import os

def find_cloud_path():
    cur = os.path.abspath(os.path.dirname(__file__))
    while True:
        candidate = os.path.join(cur, 'devops', 'cloud', 'cloud.py')
        if os.path.isfile(candidate):
            return candidate
        parent = os.path.dirname(cur)
        if parent == cur:
            raise FileNotFoundError('cloud.py introuvable')
        cur = parent

cloud_path = find_cloud_path()
spec = importlib.util.spec_from_file_location('cloud', cloud_path)
cloud = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cloud)
deploy_cloud = cloud.deploy_cloud


def test_deploy_cloud():
    result = deploy_cloud({"provider": "aws", "region": "eu-west-1"})
    assert result is True
