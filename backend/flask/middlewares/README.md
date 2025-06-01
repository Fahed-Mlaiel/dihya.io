# Middlewares Sécurité & Validation - Dihya Backend

Ce dossier contient les middlewares de sécurité : WAF, anti-DDOS, validation, audit, CORS avancé, logs structurés, hooks plugins, etc.

- `waf_protect(request)`: Protection WAF (OWASP Top 10)
- `anti_ddos(request)`: Limitation de débit, blocage IP, logs
- `validate_request(request)`: Validation schéma, anti-injection
- Extensible via plugins/API
- Conforme RGPD, logs anonymisés

Voir exemples dans `middlewares/security.py` et tests dans `tests/`.
