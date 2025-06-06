# __init__.test.py – Test d'import du point d'entrée Python validators (fixtures/helpers/validators)
def test_import_validators_init():
    import importlib
    validators = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.validators')
    assert validators is not None
