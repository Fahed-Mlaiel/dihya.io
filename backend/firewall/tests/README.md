# tests/ – Tests unitaires et d’intégration sécurité (Dihya Firewall)

Ce dossier contient les tests automatisés pour tous les modules critiques du firewall : règles, DDoS, logs, alertes, plugins, conformité RGPD, audit, accessibilité.
- `test_rules.js` : tests des règles IP/CORS/API
- `test_ddos.js` : tests du rate limiting
- `test_plugins.js` : tests des plugins sécurité
- `test_alerts.py` : tests d’envoi d’alertes
- `README.md` : documentation, bonnes pratiques, couverture
