# Exemple d’intégration du store dans un composant React

```jsx
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { userStore } from './store';

export default function Profile() {
  const user = useSelector(state => state.userStore.user);
  const dispatch = useDispatch();

  return (
    <div>
      <h2>Profil utilisateur</h2>
      {user ? <span>{user.name}</span> : <span>Non connecté</span>}
      <button onClick={() => dispatch({ type: 'LOGOUT' })}>Déconnexion</button>
    </div>
  );
}
```
