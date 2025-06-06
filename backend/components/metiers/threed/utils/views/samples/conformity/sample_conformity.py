# sample_conformity.py
"""Exemple d'utilisation des conformity views (Python)"""
from ..conformity import conformity_views
print(getattr(conformity_views, 'check_rgpd', lambda x: 'Conformity check sample')({'user': 'Alice'}))
