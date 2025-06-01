# Documentation Backend — Dihya Coding

Bienvenue dans la documentation technique du backend **Dihya Coding**.
Cette section couvre l’architecture, les modules, les bonnes pratiques, la sécurité, la conformité et l’extensibilité du backend de la plateforme.

---

## 🧩 Objectif & périmètre

- **Génération automatique** de projets numériques (Web, Mobile, IA, DevOps, Blockchain) à partir d’un cahier des charges écrit ou vocal.
- **Architecture modulaire** : chaque fonctionnalité (génération, sécurité, audit, backup, compliance, configuration, core, IA, etc.) est isolée et documentée.
- **Extensibilité** : ajout facile de nouveaux templates métiers, plugins, modules IA, routes, etc.
- **Sécurité et conformité** : RGPD, logs horodatés, anonymisation, auditabilité, gestion des secrets, fallback souverain.

---

## 📁 Structure de la documentation backend
docs/ ├── architecture.md # Schémas et explications de l’architecture backend ├── openapi.yaml # Spécification OpenAPI de l’API principale ├── user/ # Documentation utilisateur (guides, FAQ, quickstart) ├── dev_guide.md # Guide développeur (setup, contribution, tests) ├── security.md # Sécurité, RGPD, bonnes pratiques ├── faq.md # Foire aux questions techniques ├── changelog.md # Historique des évolutions backend └── README.md # Ce fichier


---

## 🔒 Sécurité & conformité

- **Authentification JWT/OAuth**, gestion des rôles, CORS, rate limiting, headers sécurisés
- **Logs horodatés** pour chaque action critique (audit, conformité RGPD)
- **Gestion des secrets** via variables d’environnement ou gestionnaire sécurisé
- **Fallback IA open-source** en cas de blocage API propriétaire
- **Auditabilité** : chaque génération de code/documentation est tracée et horodatée
- **Respect RGPD** : anonymisation, export/suppression sur demande, documentation claire

---

## 🛠️ Bonnes pratiques

- **Documenter chaque module** (README, docstrings, exemples d’utilisation)
- **Automatiser les tests** (unitaires, intégration, sécurité)
- **Limiter l’accès** aux fonctions critiques aux rôles autorisés
- **Mettre à jour la documentation** à chaque évolution du backend
- **Versionner** les exemples, **jamais les secrets réels**

---

## 📚 Liens utiles

- [Documentation utilisateur](./user/README.md)
- [Architecture backend](./architecture.md)
- [Sécurité & RGPD](./security.md)
- [Guide développeur](./dev_guide.md)
- [Spécification API (OpenAPI)](./openapi.yaml)
- [FAQ technique](./faq.md)
- [Dashboard global conformité/monitoring](../dashboard_global.md)

---

## Accès web direct à la documentation interactive

- Swagger UI : `/api/docs`
- Redoc : `/api/redoc`
- GraphQL Playground : `/api/graphql-playground`
- RGPD : `/api/rgpd/docs` (Swagger UI), `/api/rgpd/graphql` (GraphQL Playground)

### Lancer la documentation localement

```bash
# Swagger UI (nécessite fastapi, uvicorn, swagger-ui-bundle)
pip install fastapi uvicorn swagger-ui-bundle
uvicorn Dihya.backend.docs.serve_docs:app --reload
```

- Voir aussi les fichiers OpenAPI YAML de chaque module pour personnalisation avancée.

## Index OpenAPI
- [openapi_backend_index.yaml](./openapi_backend_index.yaml)

---

> Dihya Coding : conformité, sécurité, auditabilité, accessibilité, souveraineté, multilingue.

---

**Dihya Coding** – Backend souverain, modulaire, documenté.
