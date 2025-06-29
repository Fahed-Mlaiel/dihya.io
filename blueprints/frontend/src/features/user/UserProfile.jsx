// Page de profil utilisateur avancée, intégrant l’auth, l’API et l’i18n
import React from 'react';
import { useAuth } from '../../hooks/useAuth';
import { fetchAPI } from '../../services/apiService';
import { locales } from '../../i18n/i18n';

export default function UserProfile() {
  const { user, logout } = useAuth();
  const [profile, setProfile] = React.useState(null);
  React.useEffect(() => {
    if (user) fetchAPI('/api/user').then(setProfile);
  }, [user]);
  if (!user) return <div>{locales.fr.connexion} requise</div>;
  if (!profile) return <div>Chargement…</div>;
  return (
    <section>
      <h2>{locales.fr.utilisateur} : {profile.name}</h2>
      <p>Rôle : {profile.role}</p>
      <button onClick={logout}>Déconnexion</button>
    </section>
  );
}
