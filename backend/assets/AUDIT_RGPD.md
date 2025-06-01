# Dihya Backend Assets – Audit & RGPD

- Tous les assets sont audités à chaque modification (hash SHA-256, logs d’accès, conformité RGPD).
- Les logs d’accès et d’audit sont stockés dans /logs/ (anonymisés, horodatés, sans donnée personnelle).
- Chaque asset critique (modèle, config, template) est versionné et documenté.
- Les scripts d’import/export sont testés et validés (CI/CD, auditabilité).
- Les assets sont accessibles uniquement via les utilitaires sécurisés (voir main.py, index.js).
- Les assets multilingues sont validés pour l’accessibilité et la souveraineté numérique.
- Toute clé publique est vérifiée, aucune clé privée n’est stockée.
- Les assets sont prêts pour l’intégration REST/GraphQL, plugins, multitenancy.
- Documentation intégrée dans chaque asset critique (README, assets.md, labels.multilingual.json).
