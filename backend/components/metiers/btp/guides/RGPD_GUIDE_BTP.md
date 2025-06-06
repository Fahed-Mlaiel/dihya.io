# Guide RGPD BTP

Consignes pour la conformité RGPD dans le secteur BTP.

## Checklist RGPD
- Anonymisation des données sensibles (responsable, ouvriers, clients)
- Export RGPD (JSON, CSV, PDF)
- Consentement explicite (multilingue)
- Plugins RGPD (export, anonymisation, audit)
- Auditabilité des accès et modifications
- Droit à l’oubli, suppression sécurisée
- Documentation et logs structurés

## Exemples
```python
from btp import anonymiser_chantier, exporter_chantier
chantier = {...}
chantier_anonyme = anonymiser_chantier(chantier)
exporter_chantier(chantier_anonyme, format='json')
```
