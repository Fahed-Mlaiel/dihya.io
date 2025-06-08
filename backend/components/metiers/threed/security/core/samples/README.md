# Ce dossier contient des exemples ultra avancés clé en main pour le cœur métier sécurité 3D (policy, crypto, access_control).

## Structure des samples

- `policies/` : Exemples de politiques de sécurité (RBAC, ABAC, MFA)
- `crypto/` : Exemples de chiffrement/déchiffrement (AES, RSA, PBKDF2)
- `access_control/` : Exemples de gestion d’accès, sessions, MFA
- `sample_policy.js|py` : Politique de sécurité clé en main (JS/Python)
- `sample_crypto.js|py` : Exemple de chiffrement clé en main (JS/Python)
- `sample_access_control.js|py` : Exemple de contrôle d’accès clé en main (JS/Python)
- `index.js` : Point d’entrée modulaire pour tous les samples JS

## Utilisation

Importez le sample souhaité :

```js
const { policies, crypto, accessControl } = require('./core/samples');
// Utilisation : policies.sample_policy, crypto.sample_crypto, ...
```

Chaque sous-dossier contient des exemples avancés, prêts à l’emploi, pour intégration directe ou adaptation à vos besoins métiers.

---

# Ultra-advanced 3D Security Core Samples (EN)

This folder provides turn-key, advanced security samples for 3D business logic (policy, crypto, access_control). See each subfolder for ready-to-use code and integration guides.
