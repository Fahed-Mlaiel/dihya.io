# Dihya Coding – Tests Schémas & Validation

## Présentation

Ce dossier contient les tests automatisés pour les **schémas de validation** (marshmallow, pydantic, etc.) utilisés dans le backend Flask de Dihya Coding. Les schémas garantissent la cohérence, la sécurité, la conformité RGPD et la robustesse des données échangées entre les modules, les APIs et la base de données. Ils sont essentiels pour la génération multi-stack, la personnalisation métier, l’extensibilité et la sécurité globale de la plateforme.

---

## Objectifs des tests

- **Valider la conformité des données entrantes et sortantes (API, DB, plugins)**
- **Assurer la robustesse face aux payloads malformés ou inattendus**
- **Tester la compatibilité multi-stack (frontend, backend, IA, DevOps, Blockchain)**
- **Garantir la conformité RGPD (masquage, suppression, export des données sensibles)**
- **Couvrir tous les cas d’usage métier (génération, templates, utilisateurs, plugins, etc.)**
- **Vérifier la non-exposition des secrets/API dans les logs ou réponses**
- **Assurer la documentation automatique des schémas (OpenAPI/Swagger)**

---

## Structure des tests

```
/schemas/tests/
├── test_user_schema.py         # Tests schéma utilisateur (profil, rôles, RGPD)
├── test_project_schema.py      # Tests schéma projet (génération, multi-stack)
├── test_template_schema.py     # Tests schéma templates métiers (import/export)
├── test_plugin_schema.py       # Tests schéma plugins (installation, sécurité)
├── test_notification_schema.py # Tests schéma notifications (email, push, in-app)
├── test_integration_schema.py  # Tests schéma intégrations externes (webhooks, APIs)
├── test_ai_schema.py           # Tests schéma IA (payload, quotas, fallback)
├── test_security.py            # Tests sécurité (masquage, validation, accès)
├── test_rgpd_compliance.py     # Tests conformité RGPD (logs, suppression, export)
└── fixtures/                   # Données de test, mocks, configs simulées
```

---

## Bonnes pratiques

- **Tests unitaires et d’intégration** (pytest)
- **Mocks** pour simuler les payloads et données externes
- **Validation stricte** des schémas (types, formats, contraintes)
- **Logs horodatés** pour auditabilité
- **Vérification de la non-exposition des secrets**
- **Tests automatisés dans CI/CD (GitHub Actions)**
- **Documentation claire et cas d’usage reproductibles**

---

## Exemples de cas testés

- Validation d’un payload d’inscription utilisateur (email, mot de passe fort, RGPD)
- Génération de projet avec données multi-stack (frontend, backend, IA…)
- Import/export de template métier (JSON, YAML, JS)
- Installation d’un plugin avec vérification des permissions et du sandboxing
- Notification multilingue (payload, template, sécurité)
- Webhook externe (signature, schéma, sécurité)
- Suppression/export des données utilisateur (conformité RGPD)
- Sécurité : aucune fuite de clé/API dans les logs ou réponses

---

## Lancer les tests

Depuis la racine du backend Flask :

```bash
pytest app/schemas/tests/
```

---

## Contribution

- Ajouter des cas de test pour chaque nouveau schéma ou évolution métier
- Respecter la structure et les conventions de nommage
- Documenter chaque test (docstring, typage)
- Vérifier la conformité RGPD et la sécurité à chaque PR

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---