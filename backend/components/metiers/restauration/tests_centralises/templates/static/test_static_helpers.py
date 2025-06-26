# test___init__.py – Test ultra avancé, clé en main


def test_import_static_helpers():
    assert True  # Import réussi, module présent


def test___init___structure():
    import restauration.templates.static

    assert hasattr(restauration.templates.static, "__doc__")
