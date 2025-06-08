"""
Init du module fixtures.core (Python)
Synchronisation JS/Python, conformité RGPD, accessibilité, audit, CI/CD, edge cases.
Voir README.md pour la structure et les bonnes pratiques.
"""
import sys
import os
# Ajoute le dossier racine au sys.path si nécessaire pour les imports absolus
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../'))
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from .models import *
from backend.components.metiers.threed.fixtures.generators import *  # Import absolu compatible tests et prod
from .samples import *
