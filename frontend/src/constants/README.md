# 🛠️ Constants – Dihya Coding

Ce dossier centralise toutes les constantes utilisées dans l’interface Dihya Coding.  
L’organisation et la gestion des constantes garantissent : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser les valeurs réutilisables (routes, messages, limites, couleurs, etc.)
- Faciliter la maintenance, l’extensibilité et la cohérence de l’application
- Garantir la conformité RGPD (aucune donnée personnelle ou sensible)
- Optimiser la documentation et l’auditabilité des valeurs métier

---

## 📁 Structure recommandée

- `routes.js` : Routes de navigation et API
- `messages.js` : Messages d’UI, erreurs, notifications
- `limits.js` : Limites métiers (taille, durée, etc.)
- `colors.js` : Palette de couleurs partagée
- `index.js` : Export centralisé des constantes

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Ne jamais stocker de secrets, tokens ou données sensibles dans les constantes.
- **RGPD** : Aucune donnée personnelle, aucune information de tracking.
- **Extensibilité** : Ajouter de nouvelles constantes en respectant la structure et la documentation.
- **Auditabilité** : Historique des modifications via Git, commentaires JSDoc pour chaque constante.
- **Documentation** : Décrire l’usage et la portée de chaque constante.

---

## 📝 Exemple d’utilisation

```js
import { API_ROUTES } from './routes';
import { MAX_PROJECT_NAME_LENGTH } from './limits';

fetch(API_ROUTES.createProject, { ... });
```

---

## 📚 Documentation associée

- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)
- [Composants](../components/README.md)
- [Branding](../branding/README.md)

---

> **Dihya Coding : des constantes modernes, sûres, souveraines et documentées.**