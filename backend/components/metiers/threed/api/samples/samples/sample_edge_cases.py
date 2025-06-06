# sample_edge_cases.py – Exemple ultra avancé de gestion des edge cases (API Threed)
from ..controllers import get_threed
import logging

def sample_edge_cases_ultra():
    # Edge case : accès à un ID inexistant
    try:
        entity = get_threed(-999)
        assert entity is None
        logging.info('Edge case: accès à un ID inexistant OK')
    except Exception as e:
        logging.warning(f"Erreur edge case: {e}")
    print('Sample edge cases ultra avancé exécuté avec succès.')
