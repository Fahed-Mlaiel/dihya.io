"""
Tests avancés pour les tutoriels de documentation threed (Python).
"""
import importlib.util
import os

def find_tutorial_path():
    cur = os.path.abspath(os.path.dirname(__file__))
    while True:
        candidate = os.path.join(cur, 'docs', 'tutorials', 'tutorial_hello_world.py')
        if os.path.isfile(candidate):
            return candidate
        parent = os.path.dirname(cur)
        if parent == cur:
            raise FileNotFoundError('tutorial_hello_world.py introuvable')
        cur = parent

tutorial_path = find_tutorial_path()
spec = importlib.util.spec_from_file_location('tutorial_hello_world', tutorial_path)
tutorial_hello_world = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tutorial_hello_world)
hello_world_tutorial = tutorial_hello_world.hello_world_tutorial


def test_hello_world_tutorial():
    result = hello_world_tutorial()
    assert isinstance(result, str)
    assert "Exemple" in result
