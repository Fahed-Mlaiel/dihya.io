# 🧪 Tests – Module Backup Dihya Coding

Ce dossier contient les tests unitaires et d’intégration pour le module de sauvegarde (backup) de Dihya Coding.  
Les tests garantissent : robustesse, sécurité, conformité RGPD, auditabilité, extensibilité et documentation claire.

---

## 🎯 Objectifs des tests

- **Vérifier la validité et la sécurité des opérations de sauvegarde (download, list, delete)**
- **Assurer la conformité RGPD (droit à l’oubli, anonymisation des logs)**
- **Garantir la robustesse face aux erreurs et cas limites**
- **Documenter les cas d’usage métier et les scénarios critiques**

---

## 🛡️ Bonnes pratiques

- **Isolation** : Chaque test doit être indépendant et réinitialiser l’état local (mocks, localStorage).
- **Sécurité** : Tester la non-exposition de données sensibles sans consentement.
- **Auditabilité** : Vérifier la création et la suppression correcte des logs locaux.
- **Extensibilité** : Ajouter facilement de nouveaux tests pour chaque nouvelle fonctionnalité ou route.
- **Documentation** : Utiliser des descriptions claires et des docstrings pour chaque scénario.

---

## 📝 Structure recommandée

- `backup.spec.js` : Tests unitaires des fonctions API backup
- `backup.integration.spec.js` : Tests d’intégration (mock API, scénarios utilisateur)
- `__mocks__/` : Mocks pour fetch, localStorage, etc.

---

## 🧩 Exemple de test (Jest)

```js
import { downloadBackup, clearLocalBackupLogs } from '../backup';

describe('Backup API', () => {
  beforeEach(() => {
    localStorage.clear();
    // Mock fetch si besoin
  });

  it('doit valider le projectId avant téléchargement', async () => {
    await expect(downloadBackup('')).rejects.toThrow('projectId invalide');
  });

  it('doit effacer les logs locaux (RGPD)', () => {
    localStorage.setItem('backup_logs', JSON.stringify([{ action: 'download' }]));
    clearLocalBackupLogs();
    expect(localStorage.getItem('backup_logs')).toBeNull();
  });
});
```

---

## 📚 Documentation associée

- [API backup.js](../backup.js)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : des tests pour une sauvegarde robuste, conforme et transparente.**