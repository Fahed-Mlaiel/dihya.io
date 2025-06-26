# Exemples métiers – API

- `userApi.js` : Gestion des utilisateurs (getUsers, createUser)
- `projectApi.js` : Gestion des projets (getProjects, createProject)
- `authApi.js` : Authentification (login, logout, getCurrentUser)
- `apiClient.js` : Client HTTP centralisé avec gestion du token

## Exemple d’intégration
```js
import { getUsers } from './userApi';

getUsers().then(response => {
  console.log(response.data);
});
```
