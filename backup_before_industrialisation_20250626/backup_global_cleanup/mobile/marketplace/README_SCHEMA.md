# Schéma d’architecture du marketplace

```ascii
/src/marketplace
  ├── Marketplace.jsx
  ├── MarketplaceAdmin.jsx
  ├── gestion_plugins.js
  ├── gestion_templates.js
  ├── plugins/
  │     ├── analytics-plugin.json
  │     ├── pdf-export-plugin.json
  │     └── ...
  ├── templates/
  │     ├── saas-crm-template.json
  │     ├── erp-indus-template.json
  │     └── ...
  ├── README.md
  ├── README_EXEMPLES.md
  └── README_SCHEMA.md
```

- Tous les scripts sont typés, documentés, testés.
- Les templates/plugins sont versionnés, audités, prêts pour l’automatisation.
- Les composants React sont réutilisables, accessibles, intégrés à la CI/CD.
