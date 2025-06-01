# ❓ FAQ – Dihya Coding

Ce document répond aux questions fréquentes sur la sécurité, RGPD, accessibilité, CI/CD, plugins, internationalisation, auditabilité, monitoring, backup, etc.

- **Sécurité** : Comment sont gérés les secrets ? (Vault, rotation, audit)
- **RGPD** : Comment exercer le droit à l’oubli ? (fonction purge, logs effaçables)
- **Accessibilité** : La plateforme est-elle conforme WCAG ? (oui, tests automatisés)
- **CI/CD** : Comment déployer en production ? (voir guides, scripts, pipelines)
- **Plugins** : Comment ajouter une extension ? (voir PLUGINS_GUIDE.md)
- **Monitoring** : Quels outils sont utilisés ? (Prometheus, Sentry, alerting)
- **Backup** : Comment restaurer une sauvegarde ? (voir RESTORE_GUIDE.md)
- **Internationalisation** : 13+ langues supportées, fallback IA

Pour toute question non listée, voir la documentation intégrée ou contacter l’équipe technique.

---

# Dihya Coding – FAQ Technique & Conformité

**Sécurité, RGPD, accessibilité, SEO, plugins, CI/CD, multilingue, auditabilité, conformité**

## Questions fréquentes

### 1. Comment garantir la sécurité et la conformité RGPD ?
- CORS, JWT, WAF, anti-DDOS, validation stricte, audit, monitoring, backup, anonymisation, consentement, logs, portabilité, suppression, plugins RGPD.

### 2. L’API est-elle multilingue et accessible ?
- Oui, 13+ langues dynamiques, fallback, ARIA, error i18n, SEO backend, plugins accessibilité.

### 3. Comment fonctionne l’authentification ?
- JWT, OAuth2, MFA, RBAC, multitenant, logs d’audit, plugins sécurité.

### 4. Comment déployer et monitorer la plateforme ?
- Docker, Linux, GitHub Actions, Codespaces, monitoring, alertes, rollback, backup, plugins dynamiques, auditabilité.

### 5. Où trouver la documentation et les guides ?
- Voir `docs/`, API_REFERENCE.md, DEPLOYMENT.md, TEST_STRATEGY.md, guides sécurité, RGPD, accessibilité, plugins, tests, monitoring, backup, contribution.

### 6. Comment contribuer ou signaler un incident ?
- Voir CONTRIBUTING.md, INCIDENTS_GUIDE.md, auditabilité, logs, reporting multilingue, plugins, fallback IA.

---

# FAQ Dihya

## Général
**Q : À quoi sert Dihya ?**
R : Plateforme modulaire pour la gestion, l’automatisation et la conformité multi-métiers.

**Q : Quels sont les prérequis techniques ?**
R : Python 3.10+, Node.js 18+, Docker, PostgreSQL/MySQL.

## Backend
**Q : Comment lancer le backend ?**
R : `python3 run.py` ou via Docker.

**Q : Où sont les logs ?**
R : Dossier `logs/` ou via monitoring intégré.

## Frontend
**Q : Comment builder le frontend ?**
R : `npm run build` puis `npm start`.

## Sécurité
**Q : Comment activer le mode sécurisé ?**
R : Voir `.env.production` et `SECURITY.md`.

## Tests
**Q : Comment lancer les tests ?**
R : `pytest` (backend), `npm test` (frontend).

## Documentation
**Q : Où trouver la doc API ?**
R : `API_REFERENCE.md` ou `/openapi.yaml`.

---

# Foire Aux Questions (FAQ) – Dihya Coding

## Sécurité & RGPD
- **Comment mes données sont-elles protégées ?**
  Toutes les données sont chiffrées, auditables, conformes RGPD, avec monitoring et backup automatisés.
- **Comment signaler une faille de sécurité ?**
  Voir SECURITY.md ou contacter security@dihya.app.

## Accessibilité & Multilingue
- **Le service est-il accessible à tous ?**
  Oui, conforme WCAG 2.1, multilingue (13+ langues), navigation clavier, ARIA, etc.
- **Comment changer la langue de l’interface/API ?**
  Utiliser le paramètre `Accept-Language` ou le menu de langue.

## Plugins & Extensibilité
- **Puis-je ajouter des plugins ?**
  Oui, voir PLUGINS_GUIDE.md pour l’installation et la sécurité.

## CI/CD & Monitoring
- **Comment suivre l’état du service ?**
  Monitoring en temps réel, alertes, logs accessibles (voir MONITORING_GUIDE.md).

## Auditabilité & Conformité
- **Comment obtenir un rapport d’audit ?**
  Voir AUDIT_LOGGING_GUIDE.md ou demander à l’équipe conformité.

---

Pour toute autre question, consulter la documentation intégrée ou contacter support@dihya.app.
