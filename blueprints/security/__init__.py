"""
Initialisation des fonctions sécurité métier (Python)
Expose toutes les fonctions RGPD ultra avancées : purge, anonymisation, conformité, extension, doc, exemples.
"""
from .rgpd import purge_rgpd, check_rgpd, anonymize_rgpd

__all__ = ['purge_rgpd', 'check_rgpd', 'anonymize_rgpd']

# Exemple d’utilisation :
# from blueprints.security import purge_rgpd, check_rgpd, anonymize_rgpd
# data = {"id": 1, "owner": "Alice"}
# print(purge_rgpd(data))
# print(check_rgpd(data))
# print(anonymize_rgpd(data))
