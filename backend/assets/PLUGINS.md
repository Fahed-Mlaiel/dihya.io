# Dihya Backend Assets – Plugins & Extensibilité

- Les assets backend sont extensibles via un système de plugins (voir exemples dans ai/plugins.py, backend/ai/plugins.py).
- Les templates, configs, et scripts peuvent être enrichis par des plugins Python ou Node.js (ex: ajout de nouveaux modèles, formats, audits personnalisés).
- Les plugins doivent respecter la sécurité, la RGPD, et la souveraineté numérique.
- Toute extension doit être documentée et testée (voir assets.md, README.md).
- Les assets sont prêts pour l’intégration CI/CD, REST/GraphQL, multitenancy, auditabilité.
- Exemples de hooks plugins :
  - post_load_asset(asset): vérification, audit, enrichissement
  - pre_export_asset(asset): anonymisation, validation RGPD
  - on_plugin_register(plugin): contrôle de conformité, logs
- Voir la documentation intégrée pour l’API plugins et les exemples d’intégration.
