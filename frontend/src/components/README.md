# 🧩 Components – Dihya Coding

Ce dossier regroupe tous les composants React réutilisables de l’interface Dihya Coding.  
Chaque composant est conçu pour garantir : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser les composants UI pour une expérience cohérente et maintenable
- Respecter la charte graphique Dihya Coding et les standards d’accessibilité (WCAG AA)
- Optimiser la structure pour le SEO et la performance
- Faciliter l’extension, la personnalisation et la réutilisation des composants

---

## 📁 Structure recommandée

- `Navbar.jsx` : Barre de navigation principale (SEO, accessibilité, responsive)
- `Footer.jsx` : Pied de page centralisé (liens légaux, contact, SEO)
- `LanguageSwitcher.jsx` : Sélecteur de langue (accessibilité, logs RGPD)
- `ChatAssistant.jsx` : Assistant conversationnel IA (sécurité, anonymisation, auditabilité)
- `ProjectCard.jsx` : Carte projet (SEO, audit, accessibilité)
- `...` : Ajouter d’autres composants selon les besoins métier

---

## 🛡️ Bonnes pratiques

- **Design** : Cohérence visuelle, responsive, dark/light mode.
- **Accessibilité** : Contraste suffisant, focus visible, aria-labels, navigation clavier.
- **SEO** : Balises sémantiques (`nav`, `footer`, `article`), titres explicites, attributs alt pour les images.
- **Sécurité & RGPD** : Aucune donnée personnelle exposée, logs anonymisés, consentement utilisateur respecté.
- **Auditabilité** : Historique des modifications via Git, logs locaux effaçables (droit à l’oubli RGPD).
- **Extensibilité** : Ajout facile de nouveaux composants, API claire et documentée.
- **Documentation** : Docstring JSDoc pour chaque composant, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```jsx
import Navbar from './Navbar';
import Footer from './Footer';
import ProjectCard from './ProjectCard';

function App() {
  return (
    <>
      <Navbar currentLang="fr" onLangChange={lang => { /* ... */ }} />
      <main>
        <ProjectCard
          title="Mon projet"
          description="Description courte"
          updatedAt={new Date().toISOString()}
          status="En cours"
          type="Web"
        />
      </main>
      <Footer />
    </>
  );
}
```

---

## 📚 Documentation associée

- [Branding](../branding/README.md)
- [Thèmes graphiques](../branding/themes/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : des composants modernes, accessibles, souverains et conformes.**