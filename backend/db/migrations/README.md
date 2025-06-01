# Migrations – Dihya Backend DB

Ce dossier contiendra les scripts de migration de la base de données (PostgreSQL, MySQL, SQLite).

## Objectifs
- Versionner l’évolution du schéma
- Permettre upgrade/downgrade reproductibles
- Assurer la conformité RGPD, sécurité, multilingue
- Supporter CI/CD, cloud souverain, déploiement multi-stack

## Structure recommandée
- YYYYMMDD_HHMM_description.sql (ex: 20250522_1200_create_users_table.sql)
- scripts Python/Alembic pour migrations avancées

## Bonnes pratiques
- Toujours documenter chaque migration
- Tester chaque migration sur toutes les stacks supportées
- Générer un rapport d’audit après chaque migration

## 🚦 Intégration CI/CD & Audit
- Les migrations sont testées automatiquement à chaque build CI (voir `.github/workflows/ci.yml`)
- Les scripts `test_migrations.py` (pytest) et `test_migrations.sh` (bash) sont exécutés sur PostgreSQL
- Un rapport d’audit automatique est généré et archivé à chaque build (`migration_audit_report.md`)
- Exemples avancés et documentation interactive : voir `EXAMPLES_ADVANCED_MIGRATIONS.md` et `SCHEMA_INTERACTIF.md`

---

# Ultra-Industrialisation Checklist

## DWeb/IPFS
- [ ] DWeb/IPFS-Export/Import für Migrationen
- [ ] Mock- oder echte IPFS-Integration

## Sectorisation
- [ ] Mandantenfähigkeit/Sektorentrennung
- [ ] Sektorielle Szenarien und Testfälle

## RGPD/Anonymisation
- [ ] RGPD-konforme Verarbeitung
- [ ] Anonymisierungsfunktionen

## Audit & Monitoring
- [ ] Audit-Logging für alle Migrations-Operationen
- [ ] Monitoring-Hooks integriert
- [ ] Alerting-Mechanismen

## Souveränité
- [ ] Datenhoheit und -lokalisierung

## CI/CD
- [ ] CI/CD-Integration vorbereitet
- [ ] Build/Deploy-Skripte und Workflows
- [ ] Testabdeckung im CI

## Tests & Coverage
- [ ] Pytest-Tests für alle Features
- [ ] Testempfehlungen und Coverage-Ziele

## Best Practices & Beispiele
- [ ] Codebeispiele für alle Features
- [ ] Best-Practice-Abschnitt

## Weitere Anforderungen
- [ ] Nichts ausgelassen, alle Anforderungen abgedeckt
- [ ] Validierung nach manuellen Edits empfohlen

---

> **Hinweis:** Siehe zentrale Guides für Details und Beispiele.

> Voir la documentation principale dans `../README.md` et le schéma SQL dans `../database_schema.sql`.
