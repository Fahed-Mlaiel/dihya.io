# Compliance & RGPD – Sécurité 3D

Ce dossier contient :
- Sous-modules professionnels : anonymisation, purge, checklists, policies, samples
- Scripts d’anonymisation et de purge RGPD (voir sous-dossiers)
- Checklists et politiques RGPD (voir sous-dossiers)
- Exemples ultra avancés clé en main (samples)
- **Fichier `index.js` : Point d’entrée modulaire pour tous les modules JS (anonymisation, purge, checklists, policies, samples)**

## Structure professionnelle
- `anonymisation/` : scripts d’anonymisation RGPD (JS, Python)
- `purge/` : scripts de purge RGPD (JS, Bash)
- `checklists/` : checklists RGPD (JS, Markdown)
- `policies/` : politiques de sécurité (JS, Markdown)
- `samples/` : exemples ultra avancés clé en main (politiques, checklists, etc.)
- `index.js` : Import modulaire de tous les modules JS de compliance

## Utilisation

Import JS modulaire :
```js
const { anonymisation, purge, checklists, policies, samples } = require('./compliance');
// anonymisation.<...>, purge.<...>, checklists.<...>, policies.<...>, samples.policies, ...
```

---

# Compliance & RGPD – 3D Security (EN)

This folder contains anonymisation, purge, checklists, policies, and ultra-advanced samples for RGPD/3D security compliance. The `index.js` file provides a modular JS entry point for all compliance modules.
See subfolders for details.
