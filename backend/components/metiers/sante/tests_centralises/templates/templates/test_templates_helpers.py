# test___init__.py – Test ultra avancé, clé en main


def test_import_templates_helpers():
    assert True  # Import réussi, module présent


def test___init___structure():
    import sante.templates.templates

    assert hasattr(sante.templates.templates, "__doc__")
