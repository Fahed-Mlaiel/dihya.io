# Documentation API – Dihya Coding

Cette documentation décrit les endpoints principaux de l’API Dihya Coding (backend Flask & Node.js).  
Elle respecte le cahier des charges : sécurité, validation, bonnes pratiques REST, multilingue, extensibilité.

---

## Authentification

### `POST /api/auth/register`
> Inscription d’un nouvel utilisateur.

**Body JSON** :
```json
{
  "email": "user@dihya.com",
  "username": "user",
  "password": "motdepasse"
}
```
**Réponse** :  
- `201` : Utilisateur créé  
- `400` : Erreur de validation ou email déjà utilisé

---

### `POST /api/auth/login`
> Connexion utilisateur, retourne JWT access & refresh.

**Body JSON** :
```json
{
  "email": "user@dihya.com",
  "password": "motdepasse"
}
```
**Réponse** :  
- `200` : `{ "access_token": "...", "refresh_token": "...", "user": {...} }`
- `401` : Identifiants invalides

---

### `POST /api/auth/refresh`
> Rafraîchit le token d’accès JWT.

**Header** : `Authorization: Bearer <refresh_token>`

**Réponse** :  
- `200` : `{ "access_token": "..." }`
- `401` : Token refresh invalide

---

### `POST /api/auth/logout`
> Déconnexion utilisateur (invalide le JWT côté client).

**Header** : `Authorization: Bearer <access_token>`

**Réponse** :  
- `200` : Déconnexion réussie

---

## Utilisateurs

### `GET /api/users`
> Liste tous les utilisateurs (admin uniquement).

**Header** : `Authorization: Bearer <access_token>`

**Réponse** :  
- `200` : `[ { "id": 1, "email": "...", ... }, ... ]`
- `403` : Accès refusé

---

### `GET /api/users/<id>`
> Récupère un utilisateur par ID.

**Header** : `Authorization: Bearer <access_token>`

**Réponse** :  
- `200` : `{ "id": 1, "email": "...", ... }`
- `404` : Utilisateur non trouvé

---

### `GET /api/users/me`
> Récupère le profil de l’utilisateur connecté.

**Header** : `Authorization: Bearer <access_token>`

**Réponse** :  
- `200` : `{ "id": 1, "email": "...", ... }`

---

### `PUT /api/users/<id>`
> Met à jour un utilisateur (admin ou soi-même).

**Header** : `Authorization: Bearer <access_token>`

**Body JSON** :
```json
{
  "username": "nouveau_nom",
  "email": "nouveau@email.com"
}
```
**Réponse** :  
- `200` : Utilisateur mis à jour
- `400` : Erreur de validation
- `403` : Accès refusé
- `404` : Utilisateur non trouvé

---

### `DELETE /api/users/<id>`
> Supprime un utilisateur (admin uniquement).

**Header** : `Authorization: Bearer <access_token>`

**Réponse** :  
- `204` : Utilisateur supprimé
- `403` : Accès refusé
- `404` : Utilisateur non trouvé

---

## Endpoints publics

### `GET /`
> Accueil API

### `GET /api/health`
> Healthcheck (statut API)

### `GET /api/info`
> Infos générales sur l’API

### `POST /api/echo`
> Teste la réception de données (debug)

---

## Sécurité & bonnes pratiques

- Toutes les routes sensibles nécessitent un JWT valide (`Authorization: Bearer ...`)
- Validation stricte des entrées (voir erreurs 400)
- Rôles utilisateurs : admin, user, invité
- Headers de sécurité HTTP ajoutés à chaque réponse
- Rate limiting sur `/api/*`
- Multilingue : les messages d’erreur peuvent être traduits selon la langue du client

---

## Extensibilité

- Ajoutez vos propres endpoints dans les blueprints/routes
- Voir la structure du projet pour l’organisation des modules

---

## Pour aller plus loin

- Voir la documentation technique dans `docs/architecture.md`
- Pour tester l’API : utilisez Postman, Insomnia ou Swagger UI

---