# 👁️ Preview – Dihya Coding

Ce dossier regroupe les modules de gestion et génération d’aperçus pour Dihya Coding : prévisualisation de blueprints, UI, code, mobile, etc.  
Chaque module garantit : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser la génération et la gestion des aperçus dynamiques pour tous les modules générés
- Garantir la sécurité, la conformité RGPD et l’auditabilité de chaque opération de prévisualisation
- Faciliter l’extension, la maintenance et la documentation des fonctionnalités de preview

---

## 📁 Structure recommandée

- `previewManager.js` : Gestionnaire d’aperçus (génération, logs, audit, purge)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Validation stricte des types et données d’aperçu, anonymisation des logs, gestion sécurisée des tokens.
- **RGPD** : Consentement utilisateur requis, logs locaux anonymisés, droit à l’oubli (fonctions de purge).
- **Auditabilité** : Historique local des aperçus générés, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux types d’aperçus ou d’options de preview.
- **Documentation** : Docstring JSDoc pour chaque fonction, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { generatePreview, getLocalPreviewHistory } from './previewManager';

async function voirApercu() {
  const preview = await generatePreview({ type: 'web', data: { html: '<h1>Hello</h1>' } });
  const historique = getLocalPreviewHistory();
  // ...traitement, audit, logs, etc.
}
```

---

## 📚 Documentation associée

- [Blueprints](../blueprints/README.md)
- [Sécurité & RGPD](../docs/security.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : prévisualisation moderne, sécurisée, extensible et conforme RGPD pour chaque génération.**