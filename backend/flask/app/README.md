# Dihya Coding – Backend Flask

## Présentation

Ce dossier contient le **backend principal** de la plateforme Dihya Coding, développé en Flask. Il orchestre la génération automatique de projets numériques multi-stack (web, mobile, IA, DevOps, Blockchain), la gestion des utilisateurs, l’authentification, la sécurité, la conformité RGPD, l’API, la planification des tâches, la gestion des templates métiers et des plugins, la collaboration temps réel, et l’intégration avec des services externes.

---

## Objectifs & rôle du backend

- **Générer et servir des projets complets** (frontend, backend, scripts, assets)
- **Fournir une API RESTful/GraphQL sécurisée et extensible**
- **Gérer l’authentification, les rôles et la sécurité**
- **Assurer la conformité RGPD (logs, suppression/export, auditabilité)**
- **Orchestrer la génération multi-stack et la personnalisation métier**
- **Permettre l’extension via plugins, templates, scripts, intégrations**
- **Supporter la collaboration temps réel (WebSocket/SSE)**
- **Automatiser les tâches (scheduler, backup, mailing, synchronisation)**
- **Garantir la robustesse, la traçabilité et la documentation**

---

## Structure du backend

```
/app/
├── routes/            # Routes API (auth, user, project, templates, plugins, etc.)
├── models/            # Modèles de données (SQLAlchemy, Pydantic, Marshmallow)
├── schemas/           # Schémas de validation (entrée/sortie, RGPD)
├── plugins/           # Système de plugins et templates métiers
├── templates/         # Templates métiers prêts à l’emploi (health, legal, etc.)
├── scheduler/         # Planification et exécution de tâches (jobs, cron)
├── realtime/          # Collaboration et notifications temps réel (WebSocket/SSE)
├── scripts/           # Automatisations backend (génération, backup, migration)
├── tests/             # Tests unitaires et d’intégration (pytest)
├── static/            # Fichiers statiques (assets, images, docs)
├── config.py          # Configuration centralisée (env, sécurité, RGPD)
├── main.py            # Point d’entrée Flask (création app, blueprints, sécurité)
└── README.md          # (ce fichier)
```

---

## Fonctionnalités principales

- **API RESTful/GraphQL** pour tous les modules métiers
- **Authentification JWT/OAuth**, gestion des rôles (Admin, User, Invité, etc.)
- **Génération de projets multi-stack à partir d’un cahier des charges**
- **Import/export de templates métiers (JSON, YAML, JS)**
- **Marketplace de plugins et templates**
- **Gestion des utilisateurs, profils, RGPD**
- **Notifications (email, push, in-app)**
- **Collaboration temps réel (WebSocket/SSE)**
- **Scheduler pour tâches planifiées (backup, mailing, synchronisation)**
- **Sécurité avancée (CORS, anti-DDoS, rate limiting, headers)**
- **Logs horodatés, auditabilité, suppression/export RGPD**
- **Extensibilité via plugins/scripts**
- **Documentation interactive (Swagger/OpenAPI)**

---

## Sécurité & conformité RGPD

- **Validation stricte** des entrées/sorties (schemas, typage)
- **Chiffrement des données sensibles**
- **Logs auditables et suppression/export sur demande**
- **Aucune donnée sensible dans les logs ou erreurs**
- **Tests automatisés pour chaque route critique**
- **Documentation claire pour chaque module**

---

## Bonnes pratiques

- **Docstrings** et typage sur chaque fonction/méthode
- **Tests unitaires et d’intégration** pour chaque module
- **Respect des conventions de nommage et de structure**
- **Documentation claire et à jour**
- **Contribution ouverte (guide, notation, auditabilité)**

---

## Déploiement & infrastructure

- **GitHub Actions** pour CI/CD automatisé
- **GitHub Pages** pour frontend
- **Replit/Render** comme fallback backend
- **Option self-hosted et IPFS pour souveraineté**
- **Auto-backup du code (Notion API, GitHub, stockage local)**

---

## Contribution

- Toute nouvelle fonctionnalité doit être documentée et testée
- Respecter la conformité RGPD, la sécurité et la modularité
- Proposer vos améliorations via PR ou sur la marketplace communautaire

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---

*Pour toute suggestion ou amélioration, ouvrez une issue ou une PR sur GitHub.*