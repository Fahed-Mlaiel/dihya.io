# 🎨 Styles – Dihya Coding

Ce dossier regroupe tous les styles globaux et utilitaires pour Dihya Coding : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Garantir un design moderne, cohérent, accessible et responsive sur toutes les plateformes
- Optimiser l’accessibilité (contrastes, focus, dark mode, animations accessibles)
- Assurer la conformité RGPD (pas de tracking, pas de fingerprinting CSS)
- Permettre l’extension facile à de nouveaux thèmes, composants ou utilitaires

---

## 📁 Structure recommandée

- `global.css` : Styles globaux, reset, variables, dark/light, accessibilité
- `components/` : Styles spécifiques aux composants UI
- `themes/` : Thèmes personnalisés (dark, light, high-contrast…)
- `utils/` : Utilitaires CSS (helpers, mixins, classes utilitaires)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Design moderne** : Utilisation de variables CSS, responsive, typographie claire, couleurs accessibles
- **Sécurité & RGPD** : Pas de tracking, pas de fingerprinting, pas de données personnelles dans les styles
- **Auditabilité** : Documentation claire, commentaires dans le code, historique des évolutions
- **Extensibilité** : Ajout facile de nouveaux thèmes, composants ou utilitaires CSS
- **Robustesse** : Gestion des erreurs d’affichage, fallback CSS, compatibilité navigateurs
- **SEO** : Styles optimisés pour le rendu SSR, accessibilité renforcée
- **Documentation** : Commentaires pour chaque section, exemples d’utilisation

---

## 📝 Exemple d’utilisation

```css
/* Exemple d’utilisation dans global.css */
body {
  font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
  background: #f9fafb;
  color: #222;
}

/* Exemple d’utilitaire */
.sr-only {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  overflow: hidden !important;
  clip: rect(0,0,0,0) !important;
  white-space: nowrap !important;
  border: 0 !important;
}
```

---

## 📚 Documentation associée

- [global.css](./global.css)
- [components/](./components/)
- [themes/](./themes/)
- [utils/](./utils/)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : styles modernes, accessibles, robustes, extensibles et conformes RGPD pour chaque génération.**