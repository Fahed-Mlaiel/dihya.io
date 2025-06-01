# Dihya Coding – Documentation Backend Flask

## Présentation

Ce dossier contient la documentation technique et utilisateur du backend Flask de **Dihya Coding**. Il couvre l’architecture, les routes, la logique métier, la sécurité, l’extensibilité, la conformité RGPD, ainsi que les bonnes pratiques de contribution et d’auditabilité.

---

## Table des matières

- [Architecture générale](#architecture-générale)
- [Routes API principales](#routes-api-principales)
- [Sécurité & conformité RGPD](#sécurité--conformité-rgpd)
- [Extensibilité & plugins](#extensibilité--plugins)
- [Bonnes pratiques de développement](#bonnes-pratiques-de-développement)
- [Démarrage rapide](#démarrage-rapide)
- [Contribution](#contribution)
- [FAQ & Support](#faq--support)
- [Licence](#licence)

---

## Architecture générale

Le backend Flask est organisé pour garantir modularité, sécurité, auditabilité et extensibilité :

```
/app/
├── __init__.py         # Initialisation Flask, config, extensions
├── routes/             # Blueprints API (auth, user, project, templates, plugins, admin)
├── services/           # Logique métier (génération, mailing, i18n, sécurité)
├── plugins/            # Plugins métiers/extensibles (auto-chargement)
├── utils/              # Utilitaires (validation, sécurité, helpers)
├── config.py           # Configuration centralisée (env, sécurité, CORS)
└── docs/               # Documentation API et guides (ce dossier)
```

---

## Routes API principales

| Méthode | Endpoint                  | Description                                         | Authentification | Rôle requis   |
|---------|---------------------------|-----------------------------------------------------|------------------|---------------|
| POST    | `/api/auth/login`         | Connexion utilisateur (JWT)                         | Non              | -             |
| POST    | `/api/auth/register`      | Inscription utilisateur                             | Non              | -             |
| GET     | `/api/user/profile`       | Infos profil connecté                               | Oui              | User/Admin    |
| POST    | `/api/project/generate`   | Génération projet à partir d’un cahier des charges  | Oui              | User/Admin    |
| GET     | `/api/project/:id`        | Récupérer un projet généré                          | Oui              | User/Admin    |
| GET     | `/api/templates`          | Lister templates métiers disponibles                | Oui              | User/Admin    |
| POST    | `/api/templates/import`   | Importer un template métier                         | Oui              | Admin         |
| POST    | `/api/mail/send`          | Envoyer un email (test, notification)               | Oui              | User/Admin    |
| GET     | `/api/plugins`            | Lister plugins installés                            | Oui              | User/Admin    |
| POST    | `/api/plugins/install`    | Installer un plugin                                 | Oui              | Admin         |
| GET     | `/api/docs`               | Documentation API interactive (Swagger/OpenAPI)     | Non              | -             |

---

## Sécurité & conformité RGPD

- **Authentification JWT** pour toutes les routes sensibles
- **Rate limiting** (limite de requêtes par IP)
- **Validation stricte** des entrées (marshmallow/pydantic)
- **CORS** configuré (origines autorisées)
- **Headers sécurisés** (XSS, CSRF, HSTS)
- **Logs horodatés** pour auditabilité et traçabilité
- **Suppression/export des données** sur demande utilisateur (conformité RGPD)
- **Masquage des clés/API** dans les logs et réponses
- **Tests automatisés** (pytest, coverage)
- **CI/CD** via GitHub Actions

---

## Extensibilité & plugins

- **Système de plugins** pour ajouter des métiers, intégrations externes, analytics, paiement, etc.
- **Import/export de templates métiers** (JSON, YAML, JS)
- **Documentation claire** pour contribution externe
- **Marketplace** pour plugins et templates (API dédiée)

---

## Bonnes pratiques de développement

- **Docstrings** sur toutes les fonctions/méthodes
- **Typage** (type hints) pour robustesse et lisibilité
- **Validation stricte** des entrées utilisateur
- **Tests unitaires et d’intégration** pour chaque module
- **Logs horodatés** pour auditabilité
- **Respect des conventions de nommage et de structure**
- **Documentation claire et à jour**

---

## Démarrage rapide

1. Cloner le repo et installer les dépendances :
   ```bash
   cd backend/flask
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Configurer les variables d’environnement (voir `.env.example`)
3. Lancer le serveur :
   ```bash
   flask run
   ```
4. Accéder à la documentation interactive :  
   [http://localhost:5000/api/docs](http://localhost:5000/api/docs)

---

## Contribution

- Fork, branche, PR bien documentée
- Respect de la structure et des conventions
- Tests obligatoires pour toute nouvelle fonctionnalité
- Voir `/docs/CONTRIBUTING.md` pour plus de détails

---

## FAQ & Support

- Consultez la documentation interactive via `/api/docs`
- Pour toute question, ouvrez une issue sur GitHub ou contactez l’équipe via le canal officiel

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---

*Pour toute suggestion ou amélioration, merci de contribuer ou de signaler via GitHub.*