# 🛡️ Guards – Dihya Coding

Ce dossier regroupe les gardes d’accès (guards) pour la sécurisation des routes, composants et fonctionnalités sensibles dans Dihya Coding.  
Chaque garde vise : sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, design moderne et documentation claire.

---

## 🚀 Objectifs

- Protéger l’accès aux routes et composants critiques (admin, API, données sensibles…)
- Garantir la sécurité, la conformité RGPD et l’auditabilité de chaque vérification d’accès
- Faciliter l’extension, la maintenance et la documentation des stratégies de garde

---

## 📁 Structure recommandée

- `AdminGuard.js` : Garde d’accès pour routes et fonctionnalités administrateur (vérification de rôle, logs, RGPD)
- `UserGuard.js` : Garde d’accès utilisateur standard (authentification, logs, RGPD)
- `RoleGuard.js` : Garde d’accès par rôle ou groupe (flexibilité, logs, RGPD)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Vérification stricte des rôles et permissions, anonymisation des logs, gestion sécurisée des accès.
- **RGPD** : Consentement utilisateur requis pour toute opération sensible, logs locaux anonymisés, droit à l’oubli (purge).
- **Auditabilité** : Historique local des accès, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux guards ou stratégies d’accès.
- **Documentation** : Docstring JSDoc pour chaque guard, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { isAdmin, adminGuard } from './AdminGuard';

const user = { id: 'u123', roles: ['admin', 'user'] };
if (isAdmin(user)) {
  // Accès autorisé à la route admin
}

adminGuard(user, () => {
  // Callback si accès refusé (redirection, message, etc.)
});
```

---

## 📚 Documentation associée

- [Sécurité & RGPD](../docs/security.md)
- [Utils](../utils/README.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : gardes d’accès modernes, sécurisés, robustes, extensibles et conformes RGPD pour chaque génération.**