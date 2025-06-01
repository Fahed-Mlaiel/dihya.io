# 🎨 Branding – Dihya Coding

Ce dossier regroupe tous les modules, composants et assets liés à l’identité visuelle (branding) de Dihya Coding.  
L’organisation et la gestion du branding garantissent : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser la gestion des thèmes, logos, couleurs, polices et guidelines graphiques
- Offrir une expérience utilisateur cohérente, personnalisable et inclusive
- Respecter la charte graphique Dihya Coding et les standards d’accessibilité (WCAG AA)
- Permettre l’activation dynamique des thèmes (ex : Amazigh, Moderne)
- Faciliter l’extension et l’ajout de nouveaux éléments de branding

---

## 📁 Structure recommandée

- `Branding.js` : Composant centralisé pour la gestion du branding (logo, thèmes, etc.)
- `themes/` : Thèmes graphiques (amazigh.js, modern.js)
- `assets/` : Logos, couleurs, polices, templates de branding
- `tests/` : Tests unitaires et d’intégration du module branding

---

## 🛡️ Bonnes pratiques

- **Design** : Respect de la charte graphique, cohérence visuelle, responsive, dark/light mode.
- **Accessibilité** : Contraste suffisant, focus visible, aria-labels, direction du texte.
- **SEO** : Balises meta dynamiques (`theme-color`, `lang`), titres explicites, attributs alt pour les images.
- **Sécurité & RGPD** : Aucun tracking, aucune donnée personnelle dans les assets ou thèmes, logs anonymisés.
- **Auditabilité** : Historique des modifications via Git, logs locaux effaçables (droit à l’oubli RGPD).
- **Extensibilité** : Ajout facile de nouveaux thèmes, logos ou polices, propriétés personnalisables via CSS variables ou JS.

---

## 📝 Exemple d’utilisation

```js
import { setBrandingTheme, DihyaLogo } from './Branding';

// Appliquer dynamiquement un thème
setBrandingTheme('amazigh'); // ou 'modern'

// Afficher le logo accessible
<DihyaLogo alt="Logo Dihya Coding" aria-label="Logo Dihya Coding" width={64} />
```

---

## 📚 Documentation associée

- [Assets de branding](./assets/README.md)
- [Thèmes graphiques](./themes/README.md)
- [Tests branding](./tests/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : un branding moderne, souverain, accessible et conforme.**