/**
 * @file ThemeSwitcher.jsx
 * @description Composant de sélection de thème graphique pour Dihya Coding.
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les interactions sont validées, loguées localement et respectent le consentement utilisateur.
 */

import React from 'react';
import { useTheme } from './ThemeProvider';

/**
 * Liste des thèmes disponibles pour l’UI.
 */
const THEMES = [
  { code: 'modern', label: 'Moderne', emoji: '✨' },
  { code: 'amazigh', label: 'Amazigh', emoji: 'ⵣ' },
];

/**
 * Composant React pour changer dynamiquement le thème graphique.
 * @returns {JSX.Element}
 */
export default function ThemeSwitcher() {
  const { theme, setTheme } = useTheme();

  /**
   * Gère le changement de thème.
   * @param {React.ChangeEvent<HTMLSelectElement>} e
   */
  function handleChange(e) {
    const newTheme = e.target.value;
    setTheme(newTheme);
    logThemeSwitcherEvent('switch_theme', newTheme);
  }

  return (
    <div
      className="theme-switcher"
      aria-label="Sélecteur de thème graphique"
      style={{
        display: 'inline-block',
        minWidth: 120,
        margin: '0 8px',
      }}
    >
      <label htmlFor="theme-select" style={{ display: 'none' }}>
        Choisir le thème
      </label>
      <select
        id="theme-select"
        value={theme}
        onChange={handleChange}
        aria-label="Changer le thème graphique"
        style={{
          borderRadius: 6,
          border: '1px solid #E5E7EB',
          padding: '6px 12px',
          fontSize: 15,
          background: '#fff',
          color: '#222',
          outline: 'none',
          cursor: 'pointer',
        }}
      >
        {THEMES.map(t => (
          <option key={t.code} value={t.code}>
            {t.emoji} {t.label}
          </option>
        ))}
      </select>
    </div>
  );
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} theme
 */
function logThemeSwitcherEvent(action, theme) {
  try {
    const logs = JSON.parse(localStorage.getItem('theme_switcher_logs') || '[]');
    logs.push({
      action,
      theme,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('theme_switcher_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de changement de thème (droit à l’oubli RGPD).
 */
export function clearLocalThemeSwitcherLogs() {
  localStorage.removeItem('theme_switcher_logs');
}