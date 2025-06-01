# 📄 Pages – Dihya Coding

Ce dossier regroupe toutes les pages principales de l’application **Dihya Coding** : accueil, génération, aperçu, profil, connexion, inscription, erreurs, etc.  
Chaque page respecte : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs & Vision

- **Plateforme No-Code / Low-Code souveraine** : générer tout projet numérique (Web, Mobile, IA, DevOps, Blockchain) à partir d’un cahier des charges écrit ou vocal.
- **Expérience utilisateur universelle** : multilingue, responsive, accessible, inclusive (dialectes, accessibilité numérique).
- **Sécurité, RGPD & souveraineté** : validation stricte, anonymisation, logs locaux, droit à l’oubli, auditabilité, auto-hébergement, fallback open-source.
- **Extensibilité & ouverture** : templates métiers, plugins, marketplace, contribution communautaire.
- **Branding** : héritage amazigh + modernité tech, identité forte, slogan : _"De l’idée au code, en toute souveraineté."_

---

## 📁 Structure des pages

- `Home.jsx` : Accueil, présentation, navigation, logs RGPD, accès rapide à la génération.
- `Generate.jsx` : Génération de projet/module (formulaire texte/vocal, choix stack, validation, logs).
- `Preview.jsx` : Aperçu sécurisé d’un projet généré (données anonymisées, liens démo/téléchargement, logs).
- `Profile.jsx` : Profil utilisateur (gestion, export, droit à l’oubli, logs, RGPD).
- `Login.jsx` : Connexion utilisateur (validation, logs, sécurité, anonymisation).
- `Register.jsx` : Inscription utilisateur (validation, logs, sécurité, anonymisation).
- `NotFound.jsx` : Page 404 (SEO, logs, accessibilité, liens utiles).
- `README.md` : Présentation, bonnes pratiques, exemples, liens docs.

---

## 🛡️ Bonnes pratiques & exigences

- **Sécurité & RGPD** :  
  - Validation stricte des entrées, anonymisation des logs, consentement utilisateur requis, droit à l’oubli (purge locale).
  - Historique local des accès et actions, logs effaçables, documentation claire.
- **Extensibilité** :  
  - Ajout facile de nouvelles pages, routes, métiers, plugins.
  - Système de templates métiers (import/export JS, JSON, YAML).
- **Robustesse** :  
  - Gestion des erreurs, feedback utilisateur, accessibilité (ARIA, navigation clavier).
- **SEO** :  
  - Titres, descriptions et balises meta dynamiques pour chaque page.
- **Documentation** :  
  - Docstring JSDoc pour chaque page, exemples d’utilisation, liens vers guides et cahier des charges.

---

## 📝 Exemple d’utilisation (React Router)

```jsx
import Home from './Home';
import Generate from './Generate';
import Preview from './Preview';
import Profile from './Profile';
import Login from './Login';
import Register from './Register';
import NotFound from './NotFound';

<Route path="/" element={<Home />} />
<Route path="/generate" element={<Generate />} />
<Route path="/preview" element={<Preview />} />
<Route path="/profile" element={<Profile />} />
<Route path="/login" element={<Login />} />
<Route path="/register" element={<Register />} />
<Route path="*" element={<NotFound />} />
```

---

## 📚 Documentation associée

- [Layout](../layout/README.md)
- [Sécurité & RGPD](../docs/security.md)
- [Utils](../utils/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)
- [Templates métiers](https://github.com/DihyaCoding/templates)

---

## 🏆 Livrables & conformité au cahier des charges

- Code complet généré (frontend + backend + assets + routes)
- Structure GitHub modulaire et documentée
- Interface Web pour générer et tester
- Documentation utilisateur claire, traduite, et guide de contribution
- Templates métiers prêts à l’emploi (backend Python + frontend JS)
- Version démo installable/testable sans configuration complexe
- Fichiers design (Figma, images, assets…)

---

> **Dihya Coding : chaque page est pensée pour la souveraineté, la sécurité, l’accessibilité, l’extensibilité et la simplicité, pour tous.**