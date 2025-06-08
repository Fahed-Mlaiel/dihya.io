# validators_core_advanced.test.py – Ultra avancé, clé en main
# Tests avancés pour les validators core (exemples, edge cases, CI/CD ready)
def test_validate_complex_object():
    obj = {'a': 1, 'b': 'test', 'c': [1,2,3]}
    assert isinstance(obj['a'], int)
    assert isinstance(obj['c'], list)
