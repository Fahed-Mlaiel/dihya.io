"""
Test d’import du point d’entrée Python du module guides/core.
Vérifie l’import global et l’accès aux sous-modules thématiques.
"""
def test_import_core():
    import guides.core
    # Vérification d’accès à un sous-module (exemple)
    assert hasattr(guides.core, 'utils') or hasattr(guides.core, 'fixtures')
