# 🚀 Dihya – Tests End-to-End Backend (README)

Ce dossier contient les tests E2E backend : parcours utilisateur, API, plugins, métiers, multilingue, souverain, sécurisé, accessibilité.

---

## Structure
- Un dossier/scénario par parcours critique
- Tests multilingues (fr, en, ar, tzr)
- Scénarios E2E (API, plugins, sécurité, accessibilité)

---

## Méthodologie
- Tests automatisés et manuels
- Mock/fixtures pour les dépendances
- Vérification sécurité (auth, RBAC, XSS)
- Vérification accessibilité (clavier, ARIA, contrastes)

---

## Exécution
- `pytest .` ou `python -m unittest`
- `npm run e2e` ou `yarn e2e`

---

## Contribution
- Ajouter un scénario pour chaque parcours critique
- Documenter chaque cas/langue
- Vérifier la conformité et la souveraineté

---

## Contact
[qa@dihya.io](mailto:qa@dihya.io)
