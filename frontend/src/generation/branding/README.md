# 🎨 Branding – Dihya Coding

Ce dossier regroupe tous les thèmes graphiques et personnalisations d’interface pour Dihya Coding.  
Chaque thème garantit : design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser la gestion des thèmes graphiques (couleurs, typographie, composants UI)
- Garantir l’accessibilité, la sécurité, la conformité RGPD et l’auditabilité de chaque personnalisation
- Faciliter l’extension, la maintenance et la documentation des thèmes

---

## 📁 Structure recommandée

- `amazighTheme.js` : Thème graphique Amazigh (couleurs, typographie, composants)
- `modernTheme.js` : Thème graphique moderne (flat design, material design)
- `...` : Ajouter d’autres thèmes ou variantes selon les besoins métier

---

## 🛡️ Bonnes pratiques

- **Design & Accessibilité** : Contrastes élevés, typographie lisible, responsive, support du mode sombre.
- **SEO** : Métadonnées de thème, bonnes pratiques d’accessibilité, structure claire.
- **Sécurité & RGPD** : Consentement utilisateur pour toute personnalisation, logs locaux anonymisés, droit à l’oubli.
- **Auditabilité** : Historique des changements de thème, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux thèmes, API claire et typée.
- **Documentation** : Docstring JSDoc pour chaque fonction, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { applyAmazighTheme } from './amazighTheme';
import { applyModernTheme } from './modernTheme';

// Appliquer le thème Amazigh
applyAmazighTheme();

// Appliquer le thème moderne
applyModernTheme();
```

---

## 📚 Documentation associée

- [Features](../../features/README.md)
- [Blueprints](../blueprints/README.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : des thèmes modernes, accessibles, souverains et documentés.**