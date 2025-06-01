# 🛡️ API Frontend – Dihya Coding

Ce dossier regroupe toutes les APIs centralisées utilisées côté frontend pour la plateforme Dihya Coding.  
Chaque module respecte : sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire, selon le cahier des charges.

---

## 🚀 Principes & bonnes pratiques

- **Sécurité** : Authentification JWT, validation stricte des entrées, aucune donnée sensible sans consentement.
- **RGPD** : Droit à l’oubli, logs locaux anonymisés, export/suppression sur demande.
- **Auditabilité** : Toutes les actions critiques sont loguées localement (timestamp, action, id).
- **Extensibilité** : Chaque API est modulaire, facilement extensible et documentée.
- **Robustesse** : Gestion des erreurs, validation systématique, retour d’état clair.
- **Documentation** : Docstring JSDoc pour chaque fonction, exemples d’utilisation.

---

## 📚 Modules disponibles

- `auth.js` : Authentification sécurisée (inscription, login, logout, validation JWT)
- `analytics.js` : Tracking analytics RGPD-compliant (événements, logs, opt-out)
- `backup.js` : Gestion des sauvegardes (téléchargement, suppression, logs)
- `generate.js` : Génération de projets (envoi cahier des charges, templates, logs)
- `preview.js` : Prévisualisation de projets générés (récupération, suppression, logs)
- `project.js` : Gestion des projets (listing, détail, mise à jour, suppression, logs)

---

## 📝 Exemple d’utilisation

```js
import { login, logout } from './auth';
import { generateProject } from './generate';

await login({ email: 'user@dihya.com', password: '...' });
const result = await generateProject({ description: 'Site e-commerce', type: 'web' });
```

---

## 🔒 Conformité & transparence

- Toutes les APIs sont conçues pour ne jamais exposer de données sensibles sans consentement explicite.
- Les logs locaux sont anonymisés et effaçables à tout moment (voir fonctions `clearLocal*Logs`).
- Chaque module est auditable et documenté pour garantir la conformité et la maintenance.

---

> **Dihya Coding : API frontend robuste, transparente et conforme.**