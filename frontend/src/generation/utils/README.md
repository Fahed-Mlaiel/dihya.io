# 🛠️ Utils – Dihya Coding

Ce dossier regroupe les fonctions utilitaires (helpers) essentielles à la génération de code, templates et projets dans Dihya Coding : validation, formatage, anonymisation, logs, SEO, compatibilité, etc.  
Chaque utilitaire vise : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.

---

## 🚀 Objectifs

- Centraliser les helpers réutilisables pour tous les modules (AI, e-commerce, mobile, sécurité…)
- Garantir la sécurité, la conformité RGPD et l’auditabilité de chaque utilitaire
- Faciliter l’extension, la maintenance et la documentation des helpers

---

## 📁 Structure recommandée

- `validationUtils.js` : Fonctions de validation (emails, formats, sécurité, logs)
- `formatUtils.js` : Fonctions de formatage (dates, nombres, chaînes, logs)
- `anonymizeUtils.js` : Fonctions d’anonymisation des données sensibles (RGPD, logs)
- `logUtils.js` : Fonctions de gestion des logs locaux (audit, purge, RGPD)
- `seoUtils.js` : Fonctions utilitaires SEO (slugs, meta, audit)
- `compatibility.js` : Vérification de compatibilité (navigateurs, dépendances, versions)
- `generationUtils.js` : Génération d’identifiants, noms de fichiers, timestamps, etc.
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Validation stricte des entrées, anonymisation des logs, gestion sécurisée des données.
- **RGPD** : Consentement utilisateur requis pour toute opération sensible, logs locaux anonymisés, droit à l’oubli (fonctions de purge).
- **Auditabilité** : Historique local des opérations utilitaires, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux helpers ou modules utilitaires.
- **SEO** : Génération de fonctions optimisées pour le SEO si applicable.
- **Documentation** : Docstring JSDoc pour chaque utilitaire, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { validateEmail } from './validationUtils';
import { anonymizeUser } from './anonymizeUtils';
import { generateUniqueId } from './generationUtils';

const isValid = validateEmail('user@dihya.app');
const anon = anonymizeUser({ email: 'user@dihya.app', name: 'Alice' });
const uuid = generateUniqueId();
// ...utilisation dans la génération, logs, audit, etc.
```

---

## 📚 Documentation associée

- [Templates](../templates/README.md)
- [Sécurité & RGPD](../docs/security.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : utilitaires modernes, sécurisés, extensibles et conformes RGPD pour chaque génération.**