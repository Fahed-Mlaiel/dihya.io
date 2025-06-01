# logs/scripts/ — Scripts de purge & rotation des logs (Dihya Coding)

Ce dossier contient les scripts permettant de gérer la purge, l’archivage et la rotation des fichiers de logs du backend Dihya Coding.

## Objectif

- Limiter l’encombrement disque et garantir la confidentialité des logs.
- Respecter la conformité RGPD et la souveraineté numérique par une gestion maîtrisée des traces.

## Bonnes pratiques

- Ne jamais supprimer de logs critiques sans backup préalable.
- Logger chaque opération de purge ou d’archivage avec horodatage.
- Prévoir une politique de rétention configurable (nombre de jours, taille max, etc.).
- Restreindre l’accès à ces scripts aux administrateurs.
- Tester la validité des archives après rotation.
- Documenter chaque script et sa politique de gestion.

## Exemple d’utilisation

```bash
python purge_logs.py
```

---

## ✅ Checkliste Ultra-Industrialisation Logs Scripts
- [x] Purge, rotation, archivage, backup, audit, RGPD, souveraineté
- [x] DWeb/IPFS export (logs archivés, audit)
- [x] Hooks métier, sectorisation (ex: santé, éducation, ecommerce)
- [x] Tests avancés (pytest, mocks, anonymisation, sectoriel)
- [x] Intégration CI/CD (voir `.github/workflows/ci.yml`)
- [x] Monitoring, alerting, coverage, alertes anomalies
- [x] Documentation exhaustive (README, docstrings, exemples)

## 🌍 DWeb/IPFS
- Export des logs archivés sur IPFS pour auditabilité et souveraineté.
- Exemples sectoriels: santé (logs patients), éducation (logs accès), ecommerce (logs transactions).

## 🪝 Hooks métier & sectorisation
- Utilisez des hooks pour injecter la logique métier et la sectorisation dans chaque opération de purge/rotation.
- Exemple: `purge_logs(sector='santé')`

## 🔒 RGPD & anonymisation
- Jamais de données sensibles dans les logs, anonymisation, suppression/export sur demande.
- Conformité RGPD vérifiée par tests automatisés.

## 🧪 Tests & CI/CD
- Tests avancés: purge, rotation, backup, DWeb/IPFS, anonymisation, sectoriel.
- Intégration dans `.github/workflows/ci.yml` avec coverage et alerting.

## 📈 Monitoring & audit
- Logs d’accès, erreurs, purge, archivage, exportés et audités.
- Alertes sur anomalies de purge ou d’accès.

## 🏆 Best-Practice
- Documenter chaque script, versionner les politiques de rétention, valider chaque backup.
- Utiliser des mocks pour les tests DWeb/IPFS.
- Toujours valider la conformité RGPD avant déploiement.

## 📋 Exemples sectoriels
- Santé: purge logs patients, audit accès
- Éducation: rotation logs accès, anonymisation
- Ecommerce: archivage logs transactions, auditabilité

## 🔬 Recommandations tests avancés
- Mock purge/rotation, hooks métier, anonymisation, sectorisation, auditabilité, RGPD
- Couverture >95%, alerting sur échec, tests CI/CD

---

> **Dihya Coding: gestion des logs ultra-avancée, souveraine, auditable, sectorielle, RGPD, DWeb-ready, CI/CD, monitoring, documentation exhaustive.**
