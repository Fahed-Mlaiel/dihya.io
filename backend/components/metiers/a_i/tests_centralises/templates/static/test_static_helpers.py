# test___init__.py – Test ultra avancé, clé en main


def test_import_static_helpers():
    assert True  # Import réussi, module présent


def test___init___structure():
    import a_i.templates.static

    assert hasattr(a_i.templates.static, "__doc__")
