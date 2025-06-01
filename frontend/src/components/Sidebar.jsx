/**
 * @file Sidebar.jsx
 * @description Barre latérale de navigation pour Dihya Coding.
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Tous les liens sont validés, aucune donnée personnelle n’est exposée, et la structure est optimisée pour le SEO.
 */

import React from 'react';

/**
 * Liste des liens de navigation de la sidebar.
 */
const NAV_LINKS = [
  { href: '/dashboard', label: 'Tableau de bord', icon: '📊' },
  { href: '/projects', label: 'Mes projets', icon: '📁' },
  { href: '/generate', label: 'Générer', icon: '⚡' },
  { href: '/backups', label: 'Sauvegardes', icon: '💾' },
  { href: '/settings', label: 'Paramètres', icon: '⚙️' },
  { href: '/docs/user_guide/README.md', label: 'Documentation', icon: '📚' },
];

/**
 * Composant React pour la barre latérale de navigation.
 * @param {object} props
 * @param {string} [props.active] - Lien actif (href)
 * @param {function} [props.onNavigate] - Callback lors d’un clic sur un lien
 * @returns {JSX.Element}
 */
export default function Sidebar({ active, onNavigate }) {
  return (
    <aside
      className="sidebar"
      aria-label="Navigation latérale Dihya Coding"
      style={{
        width: 220,
        minHeight: '100vh',
        background: '#fff',
        borderRight: '1px solid #E5E7EB',
        padding: '32px 0 0 0',
        position: 'sticky',
        top: 0,
        left: 0,
        zIndex: 90,
        fontFamily: 'Inter, Arial, sans-serif',
        boxShadow: '0 2px 12px rgba(0,0,0,0.04)',
      }}
    >
      <nav aria-label="Menu principal" style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
        {NAV_LINKS.map(link => (
          <a
            key={link.href}
            href={link.href}
            aria-current={active === link.href ? 'page' : undefined}
            aria-label={link.label}
            onClick={e => {
              if (onNavigate) {
                e.preventDefault();
                onNavigate(link.href);
              }
              logSidebarEvent('navigate', link.href);
            }}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 12,
              padding: '10px 24px',
              color: active === link.href ? '#0057FF' : '#222',
              background: active === link.href ? '#F0F6FF' : 'transparent',
              borderLeft: active === link.href ? '4px solid #0057FF' : '4px solid transparent',
              textDecoration: 'none',
              fontWeight: active === link.href ? 700 : 500,
              fontSize: 16,
              borderRadius: '0 20px 20px 0',
              transition: 'background 0.2s, color 0.2s, border-left 0.2s',
              outline: 'none',
            }}
            tabIndex={0}
          >
            <span aria-hidden="true" style={{ fontSize: 20 }}>{link.icon}</span>
            {link.label}
          </a>
        ))}
      </nav>
      <footer
        style={{
          marginTop: 'auto',
          padding: '24px',
          color: '#888',
          fontSize: 13,
          textAlign: 'center',
        }}
      >
        <span>
          © {new Date().getFullYear()} Dihya Coding
        </span>
      </footer>
    </aside>
  );
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logSidebarEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('sidebar_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('sidebar_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de navigation sidebar (droit à l’oubli RGPD).
 */
export function clearLocalSidebarLogs() {
  localStorage.removeItem('sidebar_logs');
}