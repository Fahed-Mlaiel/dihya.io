# 🧪 Tests – Dihya Coding

Ce dossier regroupe tous les tests liés à l’infrastructure (infra) de Dihya Coding : tests unitaires, d’intégration, de sécurité, de conformité RGPD, d’auditabilité, de robustesse et d’extensibilité.  
Chaque test vise : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.

---

## 🚀 Objectifs

- Garantir la fiabilité, la sécurité et la conformité RGPD de l’infrastructure Dihya Coding
- Assurer l’auditabilité, la robustesse et la maintenabilité de tous les modules infra (DWeb, IPFS, sauvegarde, restauration…)
- Faciliter l’extension, la maintenance et la documentation des stratégies de test

---

## 📁 Structure recommandée

- `dwebService.test.js` : Tests du service DWeb (sauvegarde, restauration, logs, RGPD)
- `ipfsService.test.js` : Tests du service IPFS (sauvegarde, restauration, logs, RGPD)
- `autoBackupDWeb.test.js` : Tests d’automatisation des sauvegardes DWeb
- `autoBackupIPFS.test.js` : Tests d’automatisation des sauvegardes IPFS
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Tests de validation stricte des entrées, gestion des erreurs, anonymisation des logs.
- **RGPD** : Vérification du consentement utilisateur, tests du droit à l’oubli (purge des logs), conformité des données.
- **Auditabilité** : Vérification de la traçabilité des opérations, logs de test effaçables.
- **Extensibilité** : Ajout facile de nouveaux tests pour chaque module ou service.
- **Robustesse** : Tests de résistance, de redondance et de gestion des pannes.
- **Documentation** : Docstring JSDoc pour chaque test, exemples d’utilisation, rapports clairs.

---

## 📝 Exemple d’utilisation (Jest)

```js
import { saveToDWeb } from '../dweb/dwebService';

test('sauvegarde DWeb avec consentement', async () => {
  window.localStorage.setItem('dweb_service_feature_consent', '1');
  const result = await saveToDWeb({ projectId: 'proj_test', data: { foo: 'bar' } });
  expect(result.success).toBe(true);
});
```

---

## 📚 Documentation associée

- [DWeb](../dweb/README.md)
- [IPFS](../ipfs/README.md)
- [Sécurité & RGPD](../../docs/security.md)
- [Utils](../../utils/README.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : tests modernes, sécurisés, robustes, extensibles et conformes RGPD pour chaque génération.**