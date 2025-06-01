# Dihya Coding Backend (Flask)

Backend ultra avancé pour la gestion de projets IA, VR, AR, etc. Sécurité maximale (CORS, JWT, WAF, anti-DDOS), i18n dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es), REST/GraphQL, multitenancy, plugins, RGPD, audit, SEO, extensible, tests complets, déploiement Docker/K8s/GitHub Actions, 100% compatible Codespaces/Linux/CI.

## Fonctionnalités principales
- Sécurité : CORS, JWT, WAF, anti-DDOS, audit, validation, logs structurés
- Internationalisation dynamique (12+ langues)
- Modèle RESTful + support GraphQL
- Multitenancy, gestion des rôles (admin, user, invité)
- Plugins dynamiques (API/CLI)
- Intégration IA fallback (LLaMA, Mixtral, Mistral)
- RGPD : anonymisation, export, auditabilité
- SEO backend (robots, sitemap, logs)
- Tests unitaires, intégration, e2e
- Déploiement Docker/K8s/GitHub Actions

## Structure
- `app.py` : Entrée principale, routes, sécurité, i18n, plugins, RGPD, audit
- `middlewares/` : Sécurité, validation, WAF, anti-DDOS
- `utils/` : i18n, SEO, audit, IA fallback, GraphQL
- `plugins/` : Plugins dynamiques
- `rgpd/` : RGPD, anonymisation, export
- `tests/` : Tests complets

## Démarrage local
```bash
pip install -r requirements.txt
export JWT_SECRET_KEY=ultra-secret-key
flask run
```

## Déploiement
- Docker, K8s, GitHub Actions, fallback local

## Documentation
- Docstring, type hints, guides dans chaque dossier
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)

## RGPD & Sécurité
- Logs, anonymisation, export, audit, conformité totale

## Extensibilité
- Plugins API/CLI, hooks, templates métiers

## Contact & Contrib
Voir `CONTRIBUTING.md`, `API_SECURITY_GUIDE.md`, `PLUGINS_GUIDE.md`.
