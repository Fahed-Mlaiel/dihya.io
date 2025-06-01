# Dihya Coding – Configuration Backend Flask

## Présentation

Ce dossier contient la **configuration centralisée** du backend Flask de Dihya Coding. Il regroupe tous les paramètres essentiels à la sécurité, la conformité RGPD, la personnalisation, l’extensibilité et la robustesse de la plateforme. La configuration est conçue pour être modulaire, versionnable, auditable et facilement extensible selon les besoins métiers ou techniques.

---

## Objectifs & rôle de la configuration

- **Centraliser la gestion des paramètres sensibles et métiers**
- **Sécuriser les accès (clés, tokens, endpoints, CORS, rate limiting)**
- **Assurer la conformité RGPD (logs, audit, suppression/export)**
- **Permettre la personnalisation multi-environnement (dev, prod, test)**
- **Faciliter l’extension via plugins, templates, intégrations externes**
- **Garantir la traçabilité et la documentation des changements**

---

## Structure du dossier

```
/config/
├── config.py           # Fichier principal de configuration Flask
├── secrets.env         # Variables d’environnement sensibles (non versionnées)
├── logging.yaml        # Configuration des logs (format, niveau, audit)
├── cors.py             # Configuration CORS (origines, headers, méthodes)
├── security.py         # Paramètres sécurité (headers, rate limiting, anti-DDoS)
├── rgpd.py             # Paramètres conformité RGPD (logs, suppression/export)
├── plugins.py          # Chargement dynamique des plugins et extensions
├── scheduler.py        # Paramètres du scheduler (jobs, cron, quotas)
├── README.md           # (ce fichier)
```

---

## Bonnes pratiques de configuration

- **Séparer les secrets** (API keys, tokens) dans `secrets.env` (jamais versionné)
- **Utiliser des variables d’environnement** pour tous les paramètres sensibles
- **Documenter chaque paramètre** (usage, impact, sécurité)
- **Activer les logs horodatés et auditables**
- **Limiter les accès via CORS, rate limiting, anti-DDoS**
- **Configurer la suppression/export RGPD des logs et données**
- **Versionner la configuration (hors secrets) pour auditabilité**
- **Prévoir des valeurs par défaut sûres et des overrides par environnement**
- **Respecter la conformité RGPD et la sécurité à chaque modification**

---

## Exemples de paramètres clés

- `SECRET_KEY` : clé secrète Flask (JWT, sessions)
- `DATABASE_URL` : connexion base de données (PostgreSQL, SQLite, etc.)
- `ALLOWED_ORIGINS` : origines autorisées CORS
- `RATE_LIMIT` : limites de requêtes par IP/utilisateur
- `LOG_LEVEL` : niveau de logs (INFO, WARNING, ERROR, AUDIT)
- `MAIL_API_KEY` : clé API pour l’envoi d’emails (SendGrid, Mailgun…)
- `RGPD_EXPORT_PATH` : chemin d’export des données utilisateur
- `SCHEDULER_CRON` : configuration des tâches planifiées
- `PLUGINS_ENABLED` : liste des plugins métiers activés

---

## Sécurité & conformité RGPD

- **Aucune clé/API sensible dans le code ou les logs**
- **Suppression/export des logs et données sur demande utilisateur**
- **Auditabilité des accès et modifications**
- **Chiffrement des secrets en production**
- **Tests automatisés pour chaque modification critique**

---

## Contribution

- Documenter tout nouveau paramètre ou fichier de configuration
- Respecter la séparation secrets/configuration
- Proposer vos améliorations via PR ou sur la marketplace communautaire

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---

*Pour toute suggestion ou amélioration, ouvrez une issue ou une PR sur GitHub.*