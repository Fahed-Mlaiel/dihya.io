# Dihya Backend Django App

Ce dossier contient l'application backend Django du projet Dihya Coding. Elle fournit une API RESTful et GraphQL ultra sécurisée, multilingue, modulaire, extensible, et conforme RGPD, pour la gestion de projets IA, VR, AR, blockchain, e-commerce, etc.

## Fonctionnalités principales
- Sécurité maximale (CORS, JWT, validation, audit, WAF, anti-DDOS)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Modèle RESTful + support GraphQL
- Multitenancy + gestion des rôles (admin, user, invité)
- Intégration IA (LLaMA, Mixtral, Mistral, fallback open source)
- Optimisation SEO backend (robots, sitemap dynamique, logs structurés)
- Génération automatique de projets web, mobile, scripts IA, etc.
- Système de plugins extensible (API/CLI)
- Conformité RGPD + auditabilité (logs, anonymisation, export)
- Tests complets (unitaires, intégration, e2e)
- Déploiement GitHub Actions / Docker / K8s / fallback local
- 100% compatible GitHub Codespaces / Linux / CI

## Structure
- `routes/` : routes métiers (voir sous-dossiers)
- `plugins/` : plugins et extensions
- `tests/` : tests unitaires, intégration, e2e
- `settings/` : configuration avancée, sécurité, i18n, SEO

## Démarrage rapide
```bash
# Installation
pip install -r requirements.txt
# Lancement
python manage.py migrate && python manage.py runserver
```

## Documentation
Chaque module/fichier contient une docstring détaillée, multilingue, avec exemples d'utilisation, sécurité, i18n, SEO, RGPD, etc.

## Contribution
Voir CONTRIBUTING.md (fr/en) et CODE_OF_CONDUCT.md.

## Licence
Open source, souveraineté numérique, voir LICENSE.
