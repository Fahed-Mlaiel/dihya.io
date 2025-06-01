"""
Initialisation du module de conformité (compliance) pour Dihya Coding.

Ce package centralise les scripts et helpers d’audit RGPD, accessibilité, et conformité réglementaire.
Permet de vérifier et de documenter la conformité du backend avec les exigences légales et éthiques.

Bonnes pratiques :
- Importer ici les scripts principaux d’audit (RGPD, accessibilité, reporting)
- Ne jamais exposer de données personnelles ou sensibles dans les rapports
- Prévoir l’extensibilité pour de nouveaux audits ou contrôles
- Documenter chaque règle ou script ajouté
"""

from .audit_rgpd import generate_report as audit_rgpd_report
from .audit_accessibilite import generate_report as audit_accessibilite_report