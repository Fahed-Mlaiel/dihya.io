# 🛠️ Services – Dihya Coding

Ce dossier regroupe tous les services centraux de Dihya Coding : IA, authentification, notifications, analytics, sauvegarde, monitoring, génération, mail, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser la logique métier et les appels critiques (IA, auth, backup, monitoring…)
- Garantir la sécurité, la conformité RGPD, l’auditabilité et la robustesse de chaque service
- Permettre l’extension facile à de nouveaux services ou intégrations

---

## 📁 Structure recommandée

- `aiService.js` : Service IA (GPT, Llama, Mixtral, fallback, quota, logs)
- `authService.js` : Authentification (inscription, login, logout, logs, RGPD)
- `notificationService.js` : Notifications (toast, push, email, logs)
- `analyticsService.js` : Analytics (événements, logs, RGPD)
- `backupService.js` : Sauvegarde/restauration locale (RGPD, logs, anonymisation)
- `monitoringService.js` : Monitoring (erreurs, incidents, performances, logs)
- `generationService.js` : Génération de code, fichiers, assets (logs, RGPD)
- `mailService.js` : Envoi d’emails (notifications, logs, RGPD)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Validation stricte des entrées, anonymisation des logs, consentement utilisateur requis, droit à l’oubli (purge), pas de données sensibles dans les logs.
- **Auditabilité** : Historique local des opérations, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux services ou intégrations.
- **Robustesse** : Gestion des erreurs, feedback utilisateur, monitoring des statuts.
- **SEO** : Documentation claire et structurée pour chaque service.
- **Documentation** : Docstring JSDoc pour chaque service, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { callAI } from './aiService';
import { registerUser, loginUser } from './authService';
import { sendToast } from './notificationService';

// Appel IA
const aiResult = await callAI({ provider: 'gpt', prompt: 'Explique RGPD.' });

// Authentification
const reg = await registerUser({ email: 'test@dihya.app', password: 'S3cure!', username: 'dihya' });
const login = await loginUser({ email: 'test@dihya.app', password: 'S3cure!' });

// Notification
sendToast({ message: 'Bienvenue sur Dihya Coding !', type: 'success' });
```

---

## 📚 Documentation associée

- [aiService.js](./aiService.js)
- [authService.js](./authService.js)
- [notificationService.js](./notificationService.js)
- [analyticsService.js](./analyticsService.js)
- [backupService.js](./backupService.js)
- [monitoringService.js](./monitoringService.js)
- [generationService.js](./generationService.js)
- [mailService.js](./mailService.js)
- [Sécurité & RGPD](../security/README.md)
- [Utils](../utils/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : services modernes, robustes, extensibles et conformes RGPD pour chaque génération.**