import React from 'react';
// Sidebar avancée avec navigation dynamique et gestion des rôles
import { getUserRole } from '../../security/authService';
const links = [
  { to: '/dashboard', label: 'Dashboard', roles: ['admin', 'user'] },
  { to: '/generation', label: 'Génération', roles: ['admin', 'user'] },
  { to: '/marketplace', label: 'Marketplace', roles: ['admin', 'user', 'guest'] },
  { to: '/admin', label: 'Admin', roles: ['admin'] }
];
export default function Sidebar() {
  const role = getUserRole();
  return (
    <aside className='sidebar'>
      <ul>
        {links.filter(l => l.roles.includes(role)).map(l => (
          <li key={l.to}><a href={l.to}>{l.label}</a></li>
        ))}
      </ul>
    </aside>
  );
}
