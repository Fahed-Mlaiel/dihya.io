# 🖼️ Layout – Dihya Coding

Ce dossier regroupe tous les composants de layout (structure, navigation, header, footer, accessibilité) pour Dihya Coding.  
Chaque composant vise : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Offrir une structure d’interface cohérente, moderne et accessible pour toutes les pages de Dihya Coding
- Garantir la conformité RGPD, la sécurité, l’auditabilité et la documentation de chaque layout
- Faciliter l’extension, la maintenance et la personnalisation des layouts

---

## 📁 Structure recommandée

- `MainLayout.jsx` : Layout principal (structure, navigation, SEO, accessibilité, logs RGPD)
- `Header.jsx` : En-tête global (navigation, branding, accessibilité)
- `Footer.jsx` : Pied de page (infos légales, liens RGPD, accessibilité)
- `Sidebar.jsx` : Barre latérale (navigation avancée, modules)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Pas de données personnelles dans le layout, consentement utilisateur requis pour les logs, droit à l’oubli (purge).
- **Auditabilité** : Historique local des rendus/layouts, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux layouts ou composants de structure.
- **SEO** : Balises meta dynamiques, titres et descriptions adaptés, navigation accessible.
- **Accessibilité** : Structure ARIA, navigation clavier, focus management, responsive design.
- **Documentation** : Docstring JSDoc pour chaque composant, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```jsx
import MainLayout from './MainLayout';

function HomePage() {
  return (
    <MainLayout title="Accueil – Dihya Coding">
      <h1>Bienvenue sur Dihya Coding</h1>
      {/* ... */}
    </MainLayout>
  );
}
```

---

## 📚 Documentation associée

- [MainLayout.jsx](./MainLayout.jsx)
- [Utils](../utils/README.md)
- [Sécurité & RGPD](../docs/security.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : layouts modernes, accessibles, sécurisés, robustes, extensibles et conformes RGPD pour chaque génération.**