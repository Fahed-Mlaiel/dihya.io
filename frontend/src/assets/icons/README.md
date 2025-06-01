# 🖼️ Icons – Dihya Coding

Ce dossier contient les icônes utilisées dans l’interface de Dihya Coding.  
Les icônes sont optimisées pour un design moderne, l’accessibilité, la performance et la conformité RGPD.

---

## 🎨 Bonnes pratiques

- **Design** : Icônes SVG, adaptatives, compatibles dark/light mode, cohérentes avec l’identité Dihya.
- **Accessibilité** : Chaque icône doit avoir un titre ou un attribut `aria-label` pour les lecteurs d’écran.
- **Performance** : Utiliser des SVG inline ou des sprites pour limiter les requêtes HTTP.
- **Extensibilité** : Ajouter de nouvelles icônes en respectant la nomenclature et la structure du dossier.
- **RGPD** : Aucun tracking, aucune donnée personnelle dans les icônes ou leurs noms.
- **Auditabilité** : Historique des ajouts/modifications via le contrôle de version Git.

---

## 📁 Structure recommandée

- `svg/` : Icônes au format SVG (préféré)
- `png/` : Icônes bitmap si besoin (fallback)
- `index.js` : Export centralisé des icônes pour usage React/Vue/etc.

---

## 🛡️ Sécurité & conformité

- Toutes les icônes sont libres de droits ou créées pour Dihya Coding.
- Vérifier l’absence de métadonnées ou d’informations sensibles dans les fichiers SVG.
- Respecter la charte graphique et la politique de branding.

---

## 📝 Exemple d’utilisation (React)

```jsx
import { DihyaLogo } from './svg/DihyaLogo.svg';

function Header() {
  return <img src={DihyaLogo} alt="Logo Dihya Coding" aria-label="Logo Dihya Coding" />;
}
```

---

> **Dihya Coding : des icônes modernes, accessibles et responsables.**