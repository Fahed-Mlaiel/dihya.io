# 💾 Backup – Dihya Coding

Ce dossier regroupe tous les modules de gestion des sauvegardes (backup) pour la plateforme Dihya Coding.  
Les sauvegardes sont conçues pour garantir : sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire, selon le cahier des charges.

---

## 🚀 Fonctions couvertes

- **Sauvegarde locale** : Stockage dans le navigateur (localStorage), anonymisation, logs RGPD.
- **Sauvegarde cloud** : Téléchargement, suppression, listing via API sécurisée.
- **Sauvegarde GitHub** : Export automatique ou manuel vers un dépôt GitHub (token OAuth, logs).
- **Sauvegarde Notion** : Export des projets vers une base Notion (token, databaseId, logs).
- **Sauvegarde automatique** : Planification d’exports réguliers, consentement utilisateur, évitement des doublons.

---

## 🛡️ Sécurité & conformité

- **Consentement explicite** requis pour chaque type de sauvegarde.
- **Aucune donnée sensible** n’est stockée sans anonymisation ou consentement.
- **Logs locaux** pour chaque action (création, suppression, export), effaçables à tout moment (droit à l’oubli RGPD).
- **Validation stricte** des identifiants et des données avant toute opération.
- **Auditabilité** : Historique des actions disponible localement.

---

## 📁 Structure recommandée

- `localBackup.js` : Sauvegarde locale (navigateur)
- `autoBackup.js` : Sauvegarde automatique planifiée
- `githubBackup.js` : Sauvegarde vers GitHub
- `notionBackup.js` : Sauvegarde vers Notion
- `tests/` : Tests unitaires et d’intégration du module backup

---

## 📝 Exemple d’utilisation

```js
import { saveLocalBackup, getLocalBackup } from './localBackup';
import { backupToGitHub } from './githubBackup';

saveLocalBackup('project123', { name: 'Projet test', data: {} });
backupToGitHub('project123', { token: 'ghp_xxx', repo: 'user/repo' });
```

---

## 📚 Documentation associée

- [API backup.js](../api/backup.js)
- [Tests backup](./tests/README.md)
- [Cahier des charges Dihya Coding](../../docs/user_guide/README.md)

---

> **Dihya Coding : des sauvegardes robustes, souveraines, conformes et transparentes.**