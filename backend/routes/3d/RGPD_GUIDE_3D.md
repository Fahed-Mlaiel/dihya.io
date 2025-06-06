# GUIDE RGPD 3D – Dihya (FR)

Ce guide détaille toutes les exigences, bonnes pratiques, outils et tests RGPD pour le module 3D (API, plugins, export, anonymisation, logs, CI/CD).

## Exigences
- Export/suppression RGPD, anonymisation, logs exportables, auditabilité
- Consentement utilisateur, accès exportable, suppression sur demande
- Conformité CI/CD, auditabilité, monitoring

## Tests
- `pytest tests/test_rgpd.py`
- Export/anonymisation/suppression, audit, logs RGPD

## Contribution
- Toute nouvelle route, plugin ou template doit être conforme RGPD et testée.
- Voir LEGAL_COMPLIANCE_GUIDE.md global pour la méthodologie Dihya.
