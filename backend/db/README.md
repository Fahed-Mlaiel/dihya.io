# 🗄️ Dihya – Backend DB Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `backend/db`](#rôle-du-dossier-backenddb)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples de requêtes SQL](#exemples-de-requêtes-sql)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)
- [Ultra-Industrialisation Checklist](#ultra-industrialisation-checklist)

---

## 🗄️ Rôle du dossier `backend/db`

Ce dossier regroupe tous les schémas, scripts, fixtures et outils liés à la base de données du backend Dihya Coding.

- **Multi-stack** : PostgreSQL (recommandé), MySQL, SQLite, extensible NoSQL
- **Souveraineté** : aucun dump propriétaire, tout est open source, versionné, auditable
- **Sécurité** : conformité RGPD/NIS2, anonymisation, auditabilité, accès restreint
- **Accessibilité** : documentation multilingue (fr, en, ar, tzm), structure claire

---

## 🧠 Fonctions principales

- **Définition du schéma de données** (utilisateurs, logs, plugins, templates, sessions…)
- **Scripts de migration** (création, mise à jour, rollback, versionning)
- **Fixtures et jeux de données d’exemple** (anonymisés, multilingues, RGPD-ready)
- **Scripts d’audit et de conformité** (intégrité, anonymisation, export RGPD)
- **Tests de performance et de sécurité** (index, triggers, vues, audit)

---

## 📁 Structure recommandée

```
db/
├── database_schema.sql   # Schéma principal (multi-stack, multilingue, RGPD)
├── migrations/           # Scripts de migration (up/down, versionnés)
├── fixtures/             # Jeux de données d’exemple (anonymisés, multilingues)
├── audit/                # Scripts d’audit, d’intégrité, d’export RGPD
├── tests/                # Tests SQL, scripts de vérification, benchmarks
└── README.md             # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Respect strict du RGPD/NIS2** : anonymisation, droit à l’oubli, export, auditabilité
- **Logs horodatés** pour chaque action critique (audit, conformité)
- **Archivage sécurisé** des dumps et exports (chiffrement, rotation, RBAC)
- **Scripts d’intégrité** : vérification SHA-256, triggers de sécurité, vues d’audit
- **CI/CD-ready** : tous les scripts/tests sont compatibles GitHub Actions, Codespaces, cloud souverain

---

## 🛠️ Exemples de requêtes SQL

### Sélection des utilisateurs actifs

```sql
SELECT id, username, email, role, lang
FROM users
WHERE is_active = TRUE AND deleted_at IS NULL;
```

### Export RGPD d’un utilisateur

```sql
SELECT u.*, c.*
FROM users u
LEFT JOIN consents c ON u.id = c.user_id
WHERE u.id = 42;
```

### Insertion d’un log d’audit

```sql
INSERT INTO audit_logs (user_id, action, details, ip_address, user_agent)
VALUES (42, 'login', '{"status":"success"}', '192.168.1.1', 'Mozilla/5.0');
```

---

## 📝 Bonnes pratiques

- **Documenter chaque table et colonne** (COMMENT ON TABLE/COLUMN)
- **Traduire** les commentaires critiques (fr, en, ar, tzm)
- **Automatiser** les migrations et tests en CI/CD
- **Séparer** données de prod, test, démo (fixtures)
- **Limiter l’accès** aux dumps et exports sensibles (RBAC)
- **Vérifier l’intégrité** à chaque déploiement (scripts d’audit)
- **Exporter** tous les rapports (CSV, JSON, badge conformité)

---

## 🌍 Multilingue

- **Français** : Ce dossier est documenté en français.
- **English** : This folder is documented in English.
- **العربية** : هذا المجلد موثق باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Afaylu agi yettwarnan s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## 📚 Documentation associée

- [Schéma principal](./database_schema.sql)
- [Sécurité & RGPD](../../SECURITY.md)
- [Architecture backend](../../docs/architecture.md)
- [Scripts d’audit](../audit/scripts/README.md)
- [Décisions structurantes](../../decision_log.md)
- [Changelog technique](../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../E2E_TESTS_GUIDE.md)

---

## ✅ Ultra-Industrialisation Checklist

### DWeb/IPFS
- [ ] DWeb/IPFS-Export/Import pour DB
- [ ] Mock- ou vraie intégration IPFS

### Sectorisation
- [ ] Mandantenfähigkeit/Sektorentrennung
- [ ] Scénarios sectoriels et cas de test

### RGPD/Anonymisation
- [ ] Traitement conforme au RGPD
- [ ] Fonctions d’anonymisation

### Audit & Monitoring
- [ ] Journalisation des audits pour toutes les opérations DB
- [ ] Hooks de monitoring intégrés
- [ ] Mécanismes d'alerte

### Souveraineté
- [ ] Maîtrise et localisation des données

### CI/CD
- [ ] Intégration CI/CD préparée
- [ ] Scripts et workflows de build/deploy
- [ ] Couverture des tests dans le CI

### Tests & Coverage
- [ ] Tests Pytest pour toutes les fonctionnalités
- [ ] Recommandations de test et objectifs de couverture

### Best Practices & Exemples
- [ ] Exemples de code pour toutes les fonctionnalités
- [ ] Section des meilleures pratiques

### Autres exigences
- [ ] Rien n'est omis, toutes les exigences sont couvertes
- [ ] Validation recommandée après modifications manuelles

---

> **Remarque :** Voir les guides centraux pour les détails et les exemples.

---

**Dihya Coding** – Base de données souveraine, conforme, extensible, multilingue, prête pour la production, la démo et la contribution.

---
