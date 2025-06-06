"""
Guides Banque & Finance – Ultra avancé
--------------------------------------
Inclut guides métier, sécurité, accessibilité, RGPD, tests, plugins, multilingue, CI/CD-ready.
Import automatique pour documentation, conformité, plugins.
"""
import os

def list_guides():
    """Liste les guides disponibles dans le dossier"""
    return [f for f in os.listdir(os.path.dirname(__file__)) if f.endswith('.md')]

# Extension pour plugins/docs, conformité, audit
if __name__ == '__main__':
    print(list_guides())
