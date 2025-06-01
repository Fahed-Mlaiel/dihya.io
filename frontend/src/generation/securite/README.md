# 🛡️ Security – Dihya Coding

Ce dossier regroupe tous les modules de sécurité pour Dihya Coding : anti-DDoS, rate limiting, configuration CORS, headers HTTP, audit, logs, etc.  
Chaque module garantit : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser la gestion de la sécurité applicative et API pour tous les modules générés
- Garantir la conformité RGPD, l’auditabilité et la robustesse de chaque opération de sécurité
- Faciliter l’extension, la maintenance et la documentation des modules de sécurité

---

## 📁 Structure recommandée

- `antiDDoS.js` : Détection et blocage DDoS (logs, audit, purge)
- `rateLimit.js` : Limitation de débit par utilisateur/endpoint
- `corsConfig.js` : Configuration avancée CORS (origines, méthodes, audit)
- `headersConfig.js` : Headers HTTP de sécurité (CSP, HSTS, X-Frame, etc.)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Validation stricte des identifiants, endpoints, origines, anonymisation des logs, gestion sécurisée des tokens.
- **RGPD** : Consentement utilisateur requis, logs locaux anonymisés, droit à l’oubli (fonctions de purge).
- **Auditabilité** : Historique local des événements de sécurité, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux modules ou stratégies de sécurité.
- **Documentation** : Docstring JSDoc pour chaque fonction, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { detectDDoS } from './antiDDoS';
import { applyRateLimit } from './rateLimit';
import { getCorsConfig } from './corsConfig';
import { getSecurityHeadersConfig } from './headersConfig';

const isDDoS = detectDDoS({ userId: 'user1', endpoint: '/api/data' });
const isLimited = applyRateLimit({ userId: 'user1', endpoint: '/api/data' });
const cors = getCorsConfig({ allowedOrigins: ['https://dihya.app'] });
const headers = getSecurityHeadersConfig();
```

---

## 📚 Documentation associée

- [Sécurité & RGPD](../docs/security.md)
- [Blueprints](../blueprints/README.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : sécurité moderne, robuste, extensible et conforme RGPD pour chaque génération.**