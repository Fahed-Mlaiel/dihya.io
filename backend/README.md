# README – Dihya Backend

Ce dossier contient le backend du projet Dihya : API, logique métier, sécurité, gestion des rôles, plugins, tests, CI/CD, documentation, etc.

- Architecture modulaire, REST/GraphQL, sécurité avancée, multilingue
- Exemples d’utilisation, endpoints, scripts, tests
- Contribution, extension, personnalisation

Voir [../../README.md](../../README.md), [../README.md](../README.md)

# Dihya Coding – Backend

**La première plateforme No-Code / Low-Code souveraine, multilingue et multi-métiers.**
Slogan : _De l’idée au code, en toute souveraineté._

---

## 🚀 Objectif

Générer automatiquement tout projet numérique (Web, Mobile, IA, DevOps, Blockchain) à partir d’un cahier des charges écrit ou dicté, avec sécurité, RGPD, extensibilité et auditabilité.

---

## 🏗️ Architecture

- **Backend principal** : Flask (API REST/GraphQL, JWT, OAuth, multi-plugins)
- **Base de données** : SQLAlchemy (SQLite par défaut, extensible)
- **Sécurité** : CORS, anti-DDoS, rate limiting, audit, rôles, RGPD
- **Extensibilité** : Plugins (analytics, CMS, Stripe…), templates métiers dynamiques
- **Internationalisation** : i18n dynamique (fr, en, ar, ber, dialectes)
- **Mailing** : API (SendGrid, Mailgun…), notifications
- **SEO & Logs** : Génération automatique, logs structurés, conformité RGPD
- **Déploiement** : GitHub Actions, Codespaces, Docker, K8s, IPFS (optionnel)

---

## 🧩 Fonctionnalités principales

- **Génération multi-stack** : WebApp, API, Mobile, IA, DevOps, Blockchain
- **Entrée texte/vocale** : Multi-langue, dialectes, Speech-to-Text, GPT-4o fallback open source
- **Assistant IA** : Suggestions, correction, mémoire longue, analyse code
- **Templates métiers** : Santé, Finance, Industrie, etc. (import/export JS/JSON/YAML)
- **Marketplace** : Plugins & templates, contribution externe
- **Sécurité avancée** : JWT/OAuth, rôles, CORS, anti-DDoS, RGPD, logs auditables
- **Démo instantanée** : Preview live, lien partageable, test sans installation
- **Auto-backup** : GitHub, Notion, stockage local, IPFS/DWeb (optionnel)
- **Documentation** : Générée automatiquement (OpenAPI/Swagger), guides utilisateurs et contributeurs

---

## 📦 Structure du backend
backend/ flask/ app/ routes/ # Toutes les routes API (auth, user, generate, plugins, etc.) models/ # Modèles ORM (User, Project, Template, etc.) schemas/ # Schémas de validation (marshmallow/pydantic) services/ # Logique métier (auth, génération, mail, plugins) plugins/ # Plugins métiers (analytics, CMS, Stripe…) templates/ # Templates métiers prêts à l’emploi ai_fallback/ # Fallback IA open source (Mixtral, LLaMA, Mistral) compliance/ # RGPD, audit, reporting firewall/ # Middleware sécurité (WAF, CORS, rate limit) logs/ # Logs structurés, audit, RGPD ... requirements.txt run.py seed.py .env.example ...


---

## 🔒 Sécurité & RGPD

- **Conformité RGPD** : Export/suppression des données, logs auditables, anonymisation
- **Sécurité** : Rate limiting, CORS, anti-DDoS, validation stricte, audit, gestion des rôles
- **Auditabilité** : Logs horodatés, reporting, scripts d’audit et de purge

---

## ⚡ Démarrage rapide

```bash
cd backend/flask
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp [.env.example](http://_vscodecontentref_/1) .env
python seed.py         # (optionnel, pour données de test)
python run.py🛡️ Bonnes pratiques
Ne jamais committer de secrets dans le dépôt (<vscode_annotation details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'>util</vscode_annotation>iser .env)
Tests unitaires : lancer pytest
Documentation : voir /docs et /docs/user
Contribution : lire CONTRIBUTING.md et SECURITY.md
Extensibilité : ajouter vos plugins/templates dans app/plugins et app/templates
📚 Documentation
Architecture
API & routes
Sécurité & RGPD
Ajout de métier/plugin
Guide utilisateur
🏷️ Branding & Souveraineté
Thème : héritage amazigh + modernité tech
Licence : AGPL (open source, souveraineté numérique)
Slogan : De l’idée au code, en toute souveraineté.
🤝 Contribution
Ouvert à tous : débutants, makers, écoles, ONG, freelances.
Voir CONTRIBUTING.md.

© Dihya Coding – 2025

