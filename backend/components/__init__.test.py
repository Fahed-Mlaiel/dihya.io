# __init__.test.py – Test d'import Python du dossier components

def test_import_components():
    import backend.components
    assert hasattr(backend, 'components')
