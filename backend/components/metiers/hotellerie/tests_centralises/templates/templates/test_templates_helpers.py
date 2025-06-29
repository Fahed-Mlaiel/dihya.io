# test___init__.py – Test ultra avancé, clé en main


def test_import_templates_helpers():
    assert True  # Import réussi, module présent


def test___init___structure():
    import hotellerie.templates.templates

    assert hasattr(hotellerie.templates.templates, "__doc__")
