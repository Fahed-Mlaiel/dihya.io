# Guide de Sécurité Agriculture – Ultra avancé

Ce guide présente toutes les exigences, bonnes pratiques, outils et tests de sécurité pour le module Agriculture (API, plugins, RGPD, CI/CD).

## Exigences
- CORS strict, JWT obligatoire, WAF, anti-DDOS, validation forte
- RBAC, logs structurés, monitoring, auditabilité
- Tests d’intrusion automatisés (XSS, injection, brute-force, anti-bot, CSRF)
- Export/suppression RGPD, anonymisation, logs exportables

## Tests
- `pytest tests/test_security_e2e.py`
- Brute-force, XSS, injection, anti-bot, CSRF

## Contribution
- Toute nouvelle route, plugin ou template doit être testé pour la sécurité.
- Voir API_SECURITY_GUIDE.md pour la méthodologie Dihya.
