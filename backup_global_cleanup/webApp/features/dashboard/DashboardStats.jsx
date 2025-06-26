import React from 'react';
// Statistiques avancées du dashboard
export default function DashboardStats({ stats }) {
  return (
    <section>
      <h3>Statistiques</h3>
      <ul>
        <li>Projets générés : {stats?.projects || 0}</li>
        <li>Utilisateurs actifs : {stats?.users || 0}</li>
      </ul>
    </section>
  );
}
