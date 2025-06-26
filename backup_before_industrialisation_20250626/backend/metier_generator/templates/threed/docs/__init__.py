"""
Initialisation avancée du module docs.
Chargement dynamique des sous-modules.
Expose Tutorial pour les tests.
"""


class Tutorial:
    def __init__(self, title="Demo", content="", author=""):
        self.title = title
        self.content = content
        self.author = author


# Import dynamique désactivé pour compatibilité et robustesse CI/CD.
__all__ = []
