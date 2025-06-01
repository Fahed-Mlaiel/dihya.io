# 🛡️ Dihya – Backend Audit Scripts Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `audit/scripts`](#rôle-du-dossier-auditscripts)
- [Fonctions principales](#fonctions-principales)
- [Structure type](#structure-type)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples de scripts d’audit](#exemples-de-scripts-daudit)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)
- [Tests unitaires automatisés](#tests-unitaires-automatisés-python-nodejs-shell)

---

## 🛡️ Rôle du dossier `audit/scripts`

Ce dossier regroupe tous les scripts d’audit backend pour la plateforme Dihya : intégrité, conformité RGPD/NIS2, accessibilité, logs, etc.

- **Multi-stack** : scripts Python et Node.js, compatibles Linux, Codespaces, CI/CD
- **Souveraineté** : aucun script propriétaire, tout est open source, versionné, auditable
- **Sécurité** : vérification d’intégrité, logs, auditabilité, conformité RGPD/NIS2
- **Accessibilité** : documentation multilingue (fr, en, ar, tzm), usage CLI clair

---

## 🧠 Fonctions principales

- **Audit d’intégrité** : vérification SHA-256 de tous les assets backend (modèles, datasets, configs…)
- **Audit conformité** : vérification RGPD/NIS2, logs, anonymisation, export consentement
- **Audit accessibilité** : tests automatisés sur endpoints, assets, logs
- **Audit logs** : vérification de la traçabilité, export, anonymisation
- **Rapports multilingues** : export CSV, JSON, console, prêt pour audit externe

---

## 📦 Structure type

```
scripts/
├── check_integrity.py   # Audit d’intégrité SHA-256 (Python, multilingue, CI/CD)
├── main.py              # Point d’entrée Python (lance tous les scripts d’audit)
├── main.js              # Point d’entrée Node.js (lance tous les scripts d’audit)
├── ...                  # Autres scripts d’audit (conformité, accessibilité, logs…)
└── README.md            # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Aucune donnée personnelle réelle** ne doit être traitée sans anonymisation.
- **Logs d’audit** exportables, horodatés, multilingues.
- **Scripts versionnés** et testés (CI/CD, Codespaces, cloud souverain).
- **Rapports prêts pour audit RGPD/NIS2** (CSV, JSON, console).
- **Multilingue** : tous les messages d’audit sont traduits (fr, en, ar, tzm).

---

## 🛠️ Exemples de scripts d’audit

### Audit d’intégrité (Python)

```bash
python main.py check_integrity --lang fr --csv --json
python main.py --list
```

### Audit d’intégrité (Node.js)

```bash
node main.js --lang en --csv --json
```

### Exemple de rapport CSV

```csv
Fichier,SHA-256,Statut
models/llama2.bin,abcdef123456...,Valide
datasets/demo.csv,deadbeef9876...,Valide
configs/ia_config.yaml,1234abcd5678...,Corrompu
```

- [audit_rgpd.py](#) : Audit RGPD ultra avancé (conformité, anonymisation, consentement, export, rapport CSV/JSON)
- [audit_accessibilite.py](#) : Audit accessibilité ultra avancé (WCAG, ARIA, labels, multilingue, rapport CSV/JSON)
- [audit_logs.py](#) : Audit logs ultra avancé (traçabilité, anonymisation, structure, rapport CSV/JSON)
- [audit_plugins.py](#) : Audit plugins ultra avancé (sécurité, traçabilité, compatibilité, rapport CSV/JSON)
- [audit_webhooks.py](#) : Audit webhooks ultra avancé (sécurité, traçabilité, conformité, rapport CSV/JSON)

## Exemples d’utilisation

```bash
# Audit d’intégrité
python3 main.py check_integrity
# Audit RGPD
python3 main.py audit_rgpd
# Audit accessibilité
python3 main.py audit_accessibilite
# Audit logs
python3 main.py audit_logs
# Audit plugins
python3 main.py audit_plugins
# Audit webhooks
python3 main.py audit_webhooks
```

## Intégration CI/CD
- Ajoutez `python3 backend/audit/scripts/main.py <script>` dans vos jobs CI/CD pour automatiser les audits.
- Tous les rapports sont générés en CSV et JSON, exploitables pour audit externe, conformité, reporting souverain.

---

## 📝 Bonnes pratiques

- **Documenter chaque script** (usage, arguments, format de sortie)
- **Traduire** tous les messages (fr, en, ar, tzm)
- **Exporter** tous les rapports (CSV, JSON, console)
- **Automatiser** l’exécution en CI/CD (GitHub Actions, Codespaces)
- **Séparer** scripts Python et Node.js pour compatibilité maximale
- **Vérifier** l’intégrité et la conformité à chaque merge/déploiement

---

## 🌍 Multilingue

- **Français** : Ce dossier est documenté en français.
- **English** : This folder is documented in English.
- **العربية** : هذا المجلد موثق باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Afaylu agi yettwarnan s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## 📚 Documentation associée

- [Architecture sécurité](../../../docs/architecture.md)
- [Audit RGPD/NIS2](../../../SECURITY.md)
- [Changelog technique](../../../TECHNICAL_CHANGELOG.md)
- [Décisions structurantes](../../../decision_log.md)
- [Tests E2E](../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../WEBHOOKS_GUIDE.md)

---

## 🧪 Tests unitaires automatisés (Python, Node.js, Shell)

- **Python** : `test_audit_scripts.py` — teste chaque script d’audit, la génération et la structure des rapports, la conformité RGPD/auditabilité.
- **Node.js** : `test_audit_scripts_node.js` — vérifie l’intégrité, la génération des rapports, la robustesse RGPD/auditabilité pour `main.js`.
- **Shell** : `test_audit_scripts_shell.sh` — exécute les scripts batch, vérifie la présence et la conformité des rapports globaux, RGPD.

Tous les tests sont prêts à être intégrés dans la CI/CD (GitHub Actions, GitLab, Jenkins, Bitbucket, Azure, etc.).

---

**Dihya Coding** – Audit souverain, transparent, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
