# 📧 Mail – Dihya Coding

Ce dossier regroupe tous les modules et services liés à la gestion des emails dans Dihya Coding : envoi, réception, notifications, sécurité, conformité RGPD, auditabilité, extensibilité et documentation claire.

---

## 🚀 Objectifs

- Offrir une solution moderne, sécurisée et conforme RGPD pour l’envoi et la gestion des emails (notifications, alertes, validation…)
- Garantir la sécurité, la confidentialité, l’auditabilité et la robustesse de chaque opération email
- Faciliter l’extension, la maintenance et la personnalisation des services mail

---

## 📁 Structure recommandée

- `sendMail.js` : Service d’envoi d’emails (validation, logs, RGPD)
- `mailTemplates/` : Modèles d’emails (HTML, texte, multilingue, accessibilité)
- `mailValidator.js` : Validation des adresses et contenus (sécurité, RGPD)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Validation stricte des adresses, consentement utilisateur requis, logs anonymisés, droit à l’oubli (purge), pas de données sensibles dans les templates.
- **Auditabilité** : Historique local des envois, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux templates, langues ou stratégies d’envoi.
- **Robustesse** : Gestion des erreurs d’envoi, files d’attente, retries.
- **SEO & Accessibilité** : Templates optimisés pour l’accessibilité, contenus multilingues.
- **Documentation** : Docstring JSDoc pour chaque module, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { sendMail } from './sendMail';

await sendMail({
  to: 'user@dihya.app',
  subject: 'Bienvenue sur Dihya Coding',
  template: 'welcome',
  data: { username: 'Alice' }
});
```

---

## 📚 Documentation associée

- [mailTemplates/](./mailTemplates/)
- [mailValidator.js](./mailValidator.js)
- [Sécurité & RGPD](../docs/security.md)
- [Utils](../utils/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : emails modernes, sécurisés, robustes, extensibles et conformes RGPD pour chaque génération.**