# 🛡️ Validators – Dihya Coding

Ce dossier regroupe les validateurs (validators) utilisés dans Dihya Coding pour garantir la qualité, la sécurité et la conformité des données dans tous les modules (formulaires, API, sécurité, RGPD, etc.).  
Chaque validateur vise : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.

---

## 🚀 Objectifs

- Centraliser les fonctions de validation pour tous les modules (champs, formulaires, API, sécurité…)
- Garantir la sécurité, la conformité RGPD et l’auditabilité de chaque validation
- Faciliter l’extension, la maintenance et la documentation des stratégies de validation

---

## 📁 Structure recommandée

- `emailValidator.js` : Validation d’e-mails (format, logs, RGPD)
- `passwordValidator.js` : Validation de mots de passe (force, logs, sécurité)
- `numberValidator.js` : Validation de nombres (bornes, formats, logs)
- `dateValidator.js` : Validation de dates (formats, bornes, logs)
- `customValidator.js` : Validation personnalisée (logique métier, audit)
- `logValidatorUtils.js` : Gestion des logs de validation (audit, purge, RGPD)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Validation stricte des entrées, anonymisation des logs, gestion sécurisée des données.
- **RGPD** : Consentement utilisateur requis pour toute opération sensible, logs locaux anonymisés, droit à l’oubli (fonctions de purge).
- **Auditabilité** : Historique local des validations, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux validateurs ou stratégies de validation.
- **SEO** : Génération de validateurs optimisés pour l’accessibilité et le SEO si applicable.
- **Documentation** : Docstring JSDoc pour chaque validateur, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { emailValidator } from './emailValidator';
import { passwordValidator } from './passwordValidator';

const isEmailValid = emailValidator('user@dihya.app');
const isPasswordValid = passwordValidator('StrongPassw0rd!');
// ...utilisation dans la génération de formulaires, logs, audit, etc.
```

---

## 📚 Documentation associée

- [Utils](../utils/README.md)
- [Templates](../templates/README.md)
- [Sécurité & RGPD](../docs/security.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : validateurs modernes, sécurisés, robustes, extensibles et conformes RGPD pour chaque génération.**