# Helpers – Sécurité Blockchain (Lead Dev, clé en main)

Ce dossier regroupe les helpers utilitaires pour la sécurité blockchain.

## Fichiers inclus
- `crypto-helper.js` : chiffrement/déchiffrement AES-256
- `jwt-helper.js` : génération et vérification de JWT
- `password-helper.js` : gestion des mots de passe (hash, validation)
- `index.js` : import centralisé des helpers

## Bonnes pratiques Lead Dev
- Documenter chaque helper (usage, API, exemples)
- Versionner chaque évolution
- Utiliser les helpers dans les middlewares et services de sécurité

## Exemple d’intégration
```js
const { encrypt, decrypt } = require('./crypto-helper');
const { signJWT, verifyJWT } = require('./jwt-helper');
```

---

Pour toute contribution, suivre la checklist Lead Dev et ouvrir une Pull Request.
