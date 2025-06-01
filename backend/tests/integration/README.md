# 🔗 Dihya – Tests d’Intégration Backend (README)

Ce dossier regroupe les tests d’intégration backend : API, DB, plugins, IA, métiers, multilingue, souverain, sécurisé.

---

## Structure
- Un dossier par métier/module
- Tests multilingues (fr, en, ar, tzr)
- Scénarios d’intégration (API, DB, plugins, sécurité)

---

## Méthodologie
- Tests de bout en bout sur plusieurs modules
- Mock/fixtures pour les dépendances externes
- Vérification sécurité (auth, RBAC, secrets)

---

## Exécution
- `pytest .` ou `python -m unittest`
- `npm test` pour JS

---

## Contribution
- Ajouter un test pour chaque intégration critique
- Documenter chaque scénario/langue
- Vérifier la conformité et la souveraineté

---

## Contact
[qa@dihya.io](mailto:qa@dihya.io)
