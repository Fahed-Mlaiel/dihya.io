# 🛠️ Utils – Dihya Coding

Ce dossier regroupe tous les utilitaires JavaScript pour Dihya Coding : sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, documentation claire et bonnes pratiques.

---

## 🚀 Objectifs

- Centraliser les fonctions utilitaires réutilisables dans toute l’application
- Garantir la sécurité, la conformité RGPD, l’auditabilité et la robustesse des traitements
- Permettre l’extension facile à de nouveaux besoins métiers ou techniques

---

## 📁 Structure recommandée

- `antiDDoS.js` : Limitation anti-DDoS côté client (rate limiting, logs, RGPD)
- `api.js` : Appels API sécurisés, logs, anonymisation, RGPD
- `dataExport.js` : Export de données (JSON, CSV, TXT), logs, RGPD
- `dataPurge.js` : Purge locale des données sensibles (droit à l’oubli RGPD)
- `fallbackRouter.js` : Routage fallback client, logs, RGPD
- `headers.js` : Génération de headers HTTP/SEO sécurisés, logs, RGPD
- `originLogger.js` : Journalisation d’origine (URL, referrer, user agent), logs, RGPD
- `rateLimiter.js` : Limitation de débit générique, logs, RGPD
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Consentement utilisateur requis, anonymisation des logs, droit à l’oubli (purge), pas de données sensibles dans les logs ou exports
- **Auditabilité** : Chaque fonction est commentée, logs vérifiés et effaçables, historique des actions
- **Extensibilité** : Ajout facile de nouveaux utilitaires ou modules
- **Robustesse** : Gestion des erreurs, fallback, validation stricte des entrées
- **SEO** : Headers SEO, logs d’origine, conformité SSR
- **Documentation** : Docstring JSDoc pour chaque fonction, exemples d’utilisation

---

## 📝 Exemple d’utilisation

```js
import { apiGet, apiPost } from './api';
import { exportJSON } from './dataExport';
import { rateLimit } from './antiDDoS';

if (rateLimit('export_action')) {
  exportJSON({ foo: 'bar' }, 'export');
}
```

---

## 📚 Documentation associée

- [antiDDoS.js](./antiDDoS.js)
- [api.js](./api.js)
- [dataExport.js](./dataExport.js)
- [dataPurge.js](./dataPurge.js)
- [fallbackRouter.js](./fallbackRouter.js)
- [headers.js](./headers.js)
- [originLogger.js](./originLogger.js)
- [rateLimiter.js](./rateLimiter.js)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : utilitaires modernes, robustes, extensibles et conformes RGPD pour chaque génération.**