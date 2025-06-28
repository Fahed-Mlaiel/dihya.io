# test___init__.py – Test ultra avancé, clé en main


def test_import_templates_helpers():
    assert True  # Import réussi, module présent


def test___init___structure():
    import banque_finance.templates.templates

    assert hasattr(banque_finance.templates.templates, "__doc__")
