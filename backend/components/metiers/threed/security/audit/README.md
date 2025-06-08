# Audit & Journalisation – Sécurité 3D

Ce dossier contient :
- Sous-modules professionnels : report_templates, policies, log_examples, samples
- Scripts d’audit automatisé (voir scripts/)
- Modèles de rapports d’audit
- Guide de journalisation avancée
- Exemples de logs sécurité
- Exemples ultra avancés clé en main (samples)
- **Fichier `samples/index.js` : Point d’entrée modulaire pour tous les samples JS (logs, reports)**

## Structure professionnelle
- `report_templates/` : modèles de rapports d’audit (JS, Python, Markdown)
- `policies/` : politiques d’audit (JS, Python, Markdown)
- `log_examples/` : exemples de logs d’audit (texte, JS, Python)
- `samples/` : exemples ultra avancés clé en main (rapports, logs, etc.)
  - `index.js` : Import modulaire de tous les samples JS d’audit

## Utilisation

Import JS modulaire :
```js
const { logs, reports } = require('./audit/samples');
// logs.sample_audit_log, reports.sample_audit_report, ...
```

## Bonnes pratiques
- Activer l’audit trail sur toutes les actions sensibles
- Stocker les logs dans un espace sécurisé, chiffré
- Mettre en place une rotation et une purge régulière
- Générer des alertes en cas d’anomalie

---

# Audit & Logging – 3D Security (EN)

This folder contains audit scripts, report templates, advanced logging guides, and ultra-advanced samples. The `samples/index.js` file provides a modular JS entry point for all audit samples.

See subfolders for details.
