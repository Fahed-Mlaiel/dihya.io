# Dihya Backend Assets – Test & Validation

- Tous les assets critiques sont testés automatiquement (hash, accessibilité, multilingue, RGPD, auditabilité).
- Les scripts de test sont fournis pour Python (pytest) et Node.js (jest, mocha).
- Les assets de test (mock data, fixtures, images) sont stockés dans /tests/.
- Les tests vérifient l’intégrité, la conformité RGPD, la sécurité, la compatibilité multilingue et l’accessibilité.
- Les résultats de test sont intégrés dans la CI/CD (voir .github/workflows/).
- Exemples de tests :
  - test_load_asset.py : vérifie le chargement, le hash, l’audit
  - test_accessibility.py : vérifie l’accessibilité des templates et assets
  - test_multilingual_labels.py : vérifie la présence et la qualité des labels multilingues
- Voir la documentation intégrée pour l’exécution des tests et l’ajout de nouveaux cas.
