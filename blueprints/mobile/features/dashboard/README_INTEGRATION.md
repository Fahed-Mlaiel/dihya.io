# README_INTEGRATION.md – Dashboard

## Exemple d’intégration
```jsx
import DashboardHome from './DashboardHome';
import { useAnalytics } from '../../hooks/useAnalytics';

export default function PageDashboard() {
  const { stats } = useAnalytics();
  return <DashboardHome stats={stats} />;
}
```

## Flux utilisateur complet
1. Accès après login
2. Visualisation des stats et notifications
3. Accès aux paramètres
