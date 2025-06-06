# Guide Sécurité BTP

Bonnes pratiques de sécurité pour les applications BTP.

## Checklist sécurité
- RBAC/ABAC/PBAC (rôles, permissions, tenants)
- JWT, OAuth2, SSO, MFA
- WAF, anti-DDOS, CORS, CSP
- Auditabilité, logs structurés, SIEM
- Plugins sécurité (audit, RGPD, accessibilité)
- Sécurité CI/CD, secrets, dépendances
- RGPD : sécurité des exports, anonymisation
- Multilingue : logs, erreurs, notifications

## Exemples
```js
const { isAdmin, isChefChantier } = require('../utils/rbac');
if (!isAdmin(user)) throw new Error('Accès refusé');
```
