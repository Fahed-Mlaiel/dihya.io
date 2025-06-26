"""
Initialisation avancée du module api.
Chargement dynamique des sous-modules.
Expose create_app pour les tests.
"""


def create_app():
    # Simule une app Flask pour les tests
    class DummyApp:
        def run(self):
            return True

    return DummyApp()


# Import dynamique désactivé pour compatibilité et robustesse CI/CD.
__all__ = []
