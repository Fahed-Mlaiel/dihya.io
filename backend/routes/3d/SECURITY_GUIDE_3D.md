# GUIDE SÉCURITÉ 3D – Dihya (FR)

Ce guide détaille toutes les exigences, bonnes pratiques, outils et tests de sécurité pour le module 3D (API, plugins, RGPD, CI/CD).

## Exigences
- CORS strict, JWT obligatoire, WAF, anti-DDOS, validation stricte
- RBAC, logs structurés, monitoring, auditabilité
- Tests d’intrusion automatisés (XSS, injection, brute-force, anti-bot, CSRF)
- Export/suppression RGPD, anonymisation, logs exportables

## Tests
- `pytest tests/test_security_e2e.py`
- Vérification brute-force, XSS, injection, anti-bot, CSRF

## Contribution
- Toute nouvelle route, plugin ou template doit être testé pour la sécurité.
- Voir API_SECURITY_GUIDE.md global pour la méthodologie Dihya.
