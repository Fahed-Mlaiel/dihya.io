# ♻️ Dihya – Guide de Restauration Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Accessibilité)

---

## Table des matières

- [Introduction](#introduction)
- [Objectifs](#objectifs)
- [Principes de restauration](#principes-de-restauration)
- [Procédures de restauration](#procédures-de-restauration)
  - [Restauration frontend](#restauration-frontend)
  - [Restauration backend](#restauration-backend)
  - [Restauration mobile](#restauration-mobile)
  - [Restauration base de données](#restauration-base-de-données)
  - [Restauration assets & plugins](#restauration-assets--plugins)
  - [Restauration CI/CD & infrastructure](#restauration-cicd--infrastructure)
- [Tests & validation](#tests--validation)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce guide décrit les procédures de restauration ultra avancées pour **Dihya**.
Il garantit la souveraineté numérique, la sécurité, la conformité RGPD/NIS2, la compatibilité multi-stack (React, Flask, Node, Django, Flutter…), la portabilité (Linux, Codespaces, cloud souverain), l’accessibilité et le fallback IA open source.

---

## Objectifs

- Restauration automatisée, monitoring, rollback, auditabilité, RGPD
- Sécurité, accessibilité, multilingue, plugins, CI/CD-ready

---

## Principes de restauration

- **Sécurité** : chiffrement, RBAC, MFA, logs de restauration, auditabilité.
- **Souveraineté** : backups et restaurations sur stockage souverain (MinIO, S3 compatible, IPFS).
- **Multilingue** : procédures et messages d’erreur en fr, en, ar, tzm.
- **Accessibilité** : interfaces CLI/GUI accessibles, feedback vocal/texte.
- **Automatisation** : scripts reproductibles, CI/CD, monitoring.
- **Fallback** : restauration possible même sans cloud externe (offline, local).

---

## Procédures de restauration

### Restauration frontend

1. **Depuis artefact CI/CD**
   - Télécharger le build signé (`/artifacts/frontend/`).
   - Vérifier l’intégrité (`sha256sum`).
   - Déployer sur serveur web (`nginx`, `caddy`, etc.).
2. **Depuis backup MinIO/IPFS**
   - Récupérer le snapshot (`mc cp minio/frontend/latest.tar.gz ./`).
   - Extraire et déployer.

### Restauration backend

1. **Depuis artefact CI/CD**
   - Télécharger le build (`/artifacts/backend/`).
   - Vérifier la signature.
   - Déployer via Docker Compose/Kubernetes.
2. **Depuis backup souverain**
   - Récupérer l’image (`mc cp minio/backend/latest.tar.gz ./`).
   - Restaurer la configuration (`.env`, secrets chiffrés).

### Restauration mobile

- **APK/IPA** : récupérer le build signé, déployer sur store ou MDM.
- **Flutter** : `flutter build apk` ou `flutter build ios` puis déploiement.

### Restauration base de données

1. **PostgreSQL**
   - `pg_restore -U <user> -d <db> <backup.dump>`
2. **MongoDB**
   - `mongorestore --uri <uri> <backup_dir>`
3. **Fallback local**
   - Restaurer dump chiffré depuis `/backups/` local ou MinIO.

### Restauration assets & plugins

- **Assets** : restaurer `/assets/` depuis backup MinIO/IPFS.
- **Plugins** : restaurer `/plugins/`, vérifier signatures, relancer le service.

### Restauration CI/CD & infrastructure

- **Workflows GitHub Actions** : restaurer `.github/workflows/` depuis backup Git.
- **Secrets** : restaurer via vault souverain (HashiCorp Vault, SOPS, etc.).
- **Monitoring** : restaurer dashboards Prometheus/Grafana via export JSON.

---

## Tests & validation

- [ ] Vérifier l’intégrité (hash, signature)
- [ ] Vérifier les logs de restauration (aucune erreur, horodatage)
- [ ] Tester l’accès (frontend, backend, mobile, API)
- [ ] Vérifier la conformité RGPD/NIS2 (logs, consentement, purge)
- [ ] Tester fallback IA open source (si cloud KO)
- [ ] Vérifier accessibilité (audit axe-core, navigation clavier)
- [ ] Vérifier multilingue (fr, en, ar, tzm)

---

## Templates & exemples

### Template de rapport de restauration

```
- Date/Heure : YYYY-MM-DD HH:MM
- Stack restaurée : Frontend / Backend / Mobile / DB / Plugins / Infra
- Source backup : CI/CD / MinIO / IPFS / Local
- Responsable :
- Intégrité : OK / KO (preuve : hash/signature)
- Tests post-restauration : OK / KO (preuve : capture/log)
- Problèmes rencontrés :
- Commentaire :
```

### Exemple rempli

```
- Date/Heure : 2025-05-20 22:00
- Stack restaurée : Backend
- Source backup : MinIO
- Responsable : @devops-lead
- Intégrité : OK (sha256:abcd1234)
- Tests post-restauration : OK (voir /logs/restore/2025-05-20_backend.log)
- Problèmes rencontrés : Aucun
- Commentaire : Restauration validée, conformité RGPD OK
```

---

## Multilingue

- **Français** : Ce guide est disponible en français.
- **English** : This guide is available in English.
- **العربية** : هذا الدليل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-restore
- **Email** : restore@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/votre-org/dihya/issues)

---

> **Ce guide est validé pour la production. Toute modification doit être soumise via PR et validée par le DevOps Lead et le DPO.**

# Guide de Restauration Dihya

- Procédures de restauration (base, assets, configs, secrets)
- Tests de restauration, rollback, alertes
- Exemples de scripts (bash, Python)
- Intégration monitoring, reporting

Voir [BACKUP_GUIDE.md](BACKUP_GUIDE.md), [MONITORING_GUIDE.md](MONITORING_GUIDE.md)

---

## Documentation intégrée

- Voir aussi: BACKUP_GUIDE.md, AUDIT_LOGGING_GUIDE.md, MONITORING_GUIDE.md

---

Pour toute question, contacter l’équipe backup.
