# 🎨 Thèmes – Dihya Coding

Ce dossier regroupe les thèmes graphiques disponibles pour l’interface de Dihya Coding.  
Chaque thème garantit : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Offrir une expérience utilisateur personnalisable et inclusive
- Respecter la charte graphique Dihya Coding et les standards d’accessibilité (WCAG AA)
- Permettre l’activation dynamique des thèmes (ex : Amazigh, Moderne)
- Faciliter l’extension et l’ajout de nouveaux thèmes

---

## 📁 Structure recommandée

- `amazigh.js` : Thème Amazigh (couleurs, polices, styles, accessibilité, conformité RGPD)
- `modern.js` : Thème moderne (design épuré, SEO, accessibilité, robustesse)
- `README.md` : Documentation des bonnes pratiques et de l’API thème

---

## 🛡️ Bonnes pratiques

- **Design** : Respect de la charte graphique, cohérence visuelle, responsive, dark/light mode.
- **Accessibilité** : Contraste suffisant, focus visible, aria-labels, direction du texte.
- **SEO** : Balises meta dynamiques (`theme-color`, `lang`), titres explicites.
- **Sécurité & RGPD** : Aucun tracking, aucune donnée personnelle dans les thèmes, logs d’application anonymisés.
- **Auditabilité** : Historique des modifications via Git, documentation claire des propriétés.
- **Extensibilité** : Ajout facile de nouveaux thèmes, propriétés personnalisables via CSS variables ou JS.

---

## 📝 Exemple d’utilisation

```js
import { amazighTheme, applyAmazighTheme } from './amazigh';
import { modernTheme, applyModernTheme } from './modern';

// Appliquer dynamiquement un thème
applyAmazighTheme(); // ou applyModernTheme()
```

---

## 📚 Documentation associée

- [Charte graphique Dihya Coding](../../assets/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : des thèmes modernes, accessibles, souverains et conformes.**