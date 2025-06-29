# README_INTEGRATION.md – Auth

## Exemple d’intégration
```jsx
import { useAuth } from '../../hooks/useAuth';
import LoginForm from './LoginForm';

export default function PageLogin() {
  const { login, error } = useAuth();
  return <LoginForm onSubmit={login} error={error} />;
}
```

## Flux utilisateur complet
1. Saisie email/mot de passe
2. Validation via useAuth
3. Redirection dashboard si succès
4. Message d’erreur sinon
