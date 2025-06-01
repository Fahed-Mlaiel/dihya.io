# Déploiement Dihya

Ce document explique comment déployer l’ensemble du projet Dihya (backend, frontend, services, CI/CD, sécurité, etc.) dans un environnement de production ou de test.

## Prérequis
- Docker et docker-compose (recommandé)
- Python 3.10+, Node.js 18+, npm
- Accès aux variables d’environnement (voir `.env.example`)
- Accès à la base de données (PostgreSQL/MySQL)

## Étapes générales
1. **Cloner le dépôt**
2. **Configurer les variables d’environnement**
3. **Installer les dépendances**
   - Backend : `pip install -r requirements.txt`
   - Frontend : `npm install`
4. **Lancer les migrations** (si base de données)
5. **Démarrer les services**
   - Avec Docker : `docker-compose up -d`
   - Sans Docker :
     - Backend : `python3 run.py`
     - Frontend : `npm run build && npm start`
6. **Accéder à l’application**
   - Backend : http://localhost:5000
   - Frontend : http://localhost:3000

## CI/CD
- Voir `.github/workflows/` pour la configuration GitHub Actions.
- Les tests sont lancés automatiquement à chaque push.

## Sécurité
- Changer les secrets par défaut dans `.env.production`.
- Activer HTTPS en production.
- Voir `SECURITY.md` et `API_SECURITY_GUIDE.md`.

## Monitoring & Logs
- Voir `MONITORING_GUIDE.md` et `LOGGING_GUIDE.md`.

---

# 🚀 Guide de Déploiement – Dihya Coding

Ce guide décrit les procédures de déploiement sécurisé, automatisé et conforme de Dihya Coding (Linux, CI/CD, Docker, Cloud, etc.).

- **Sécurité** : Secrets via gestionnaire sécurisé, audit, monitoring, backup, WAF, anti-DDOS, validation, logging, RBAC, multitenancy.
- **RGPD** : Aucune donnée personnelle dans les artefacts, logs effaçables, consentement, documentation claire.
- **Accessibilité** : Scripts et guides accessibles, internationalisation dynamique.
- **CI/CD** : Pipelines automatisés, rollback, tests, monitoring, conformité production.
- **Extensibilité** : Plugins, hooks, déploiement multi-environnements.

## Procédure type

1. Préparer l’environnement (Linux, Docker, secrets, accès RBAC)
2. Lancer le pipeline CI/CD (`make deploy` ou via GitHub Actions)
3. Vérifier le monitoring, les logs, l’accessibilité, la conformité RGPD
4. Backup automatique, audit, alerting

## Pour la procédure complète, voir la documentation interne et les scripts CI/CD.

---

Pour toute question, contacter l’équipe DevSecOps.
