// Dashboard avancé, intégrant l’auth, l’API, le thème, et la sécurité
import React from 'react';
import { useAuth } from '../../hooks/useAuth';
import { fetchAPI } from '../../services/apiService';
import { getUserRole } from '../../security/authService';
import { locales } from '../../i18n/i18n';

export default function DashboardHome() {
  const { user } = useAuth();
  const [stats, setStats] = React.useState(null);
  React.useEffect(() => {
    if (user) fetchAPI('/api/dashboard').then(setStats);
  }, [user]);
  if (!user) return <div>Accès refusé</div>;
  if (!stats) return <div>Chargement…</div>;
  return (
    <main>
      <h2>Dashboard ({getUserRole()})</h2>
      <div>Projets générés : {stats.projects}</div>
      <div>Utilisateurs actifs : {stats.users}</div>
    </main>
  );
}
