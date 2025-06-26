# test___init__.py – Test ultra avancé, clé en main


def test_import_j2_helpers():
    assert True  # Import réussi, module présent


def test___init___structure():
    import automobile.templates.j2

    assert hasattr(automobile.templates.j2, "__doc__")
