# Middlewares – Sécurité Blockchain (Lead Dev, clé en main)

Ce dossier regroupe les middlewares de sécurité pour la blockchain.

## Fichiers inclus
- `auth-middleware.js` : authentification JWT
- `rate-limit-middleware.js` : rate limiting (limitation de débit)
- `cors-middleware.js` : gestion CORS
- `audit-middleware.js` : audit et traçabilité
- `index.js` : import centralisé des middlewares

## Bonnes pratiques Lead Dev
- Documenter chaque middleware (usage, API, exemples)
- Versionner chaque évolution
- Utiliser les middlewares dans l’API, les routes, les services

## Exemple d’intégration
```js
const { AuthMiddleware, RateLimitMiddleware } = require('./index');
app.use(AuthMiddleware);
app.use(RateLimitMiddleware);
```

---

Pour toute contribution, suivre la checklist Lead Dev et ouvrir une Pull Request.
