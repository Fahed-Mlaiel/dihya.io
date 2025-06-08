# Cœur métier sécurité – 3D Security Core

Ce dossier contient :
- Politiques de sécurité (RBAC, ABAC, MFA)
- Gestion des accès et sessions
- Chiffrement/déchiffrement (AES, RSA, PBKDF2)
- Fonctions utilitaires sécurité
- Exemples d’intégration API
- **Dossier `samples/` : Exemples ultra avancés clé en main (policies, crypto, access_control)**
- **Fichier `index.js` : Point d’entrée modulaire pour tous les modules JS (policy, crypto, access_control, samples)**

## Structure
- `policy/` : Politiques de sécurité, modèles, helpers
- `crypto/` : Fonctions de chiffrement, gestion des clés
- `access_control/` : Gestion des accès, sessions, MFA
- `samples/` : Exemples clé en main (voir README dédié)
- `index.js` : Import modulaire de tous les modules JS du core

## Utilisation

Import JS modulaire :
```js
const { policy, crypto, accessControl, samples } = require('./core');
// policy.<...>, crypto.<...>, accessControl.<...>, samples.policies, ...
```

## Bonnes pratiques
- Séparer logique métier et logique sécurité
- Utiliser des algorithmes éprouvés (jamais maison)
- Documenter chaque politique et point d’entrée critique
- Utiliser les samples pour accélérer l’intégration et les tests

---

# 3D Security Core (EN)

This folder contains core security logic, policies, encryption utilities, and advanced samples for direct integration. See `samples/` for ready-to-use code. The `index.js` file provides a modular JS entry point for all core modules.
