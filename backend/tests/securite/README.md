# 🛡️ Dihya – Tests de Sécurité Backend (README)

Ce dossier regroupe les tests de sécurité backend : XSS, CSRF, RBAC, secrets, métiers, multilingue, souverain, conformité.

---

## Structure
- Un test par type de vulnérabilité/métier
- Tests multilingues (fr, en, ar, tzr)
- Scénarios sécurité (auth, RBAC, secrets, plugins)

---

## Méthodologie
- Tests automatisés et manuels
- Audit de code, fuzzing, injection
- Vérification conformité (RGPD, NIS2, souveraineté)

---

## Exécution
- `pytest .` ou `python -m unittest`
- `npm run securite` ou `yarn securite`

---

## Contribution
- Ajouter un test pour chaque vulnérabilité critique
- Documenter chaque scénario/langue
- Vérifier la conformité et la souveraineté

---

## Contact
[security@dihya.io](mailto:security@dihya.io)
