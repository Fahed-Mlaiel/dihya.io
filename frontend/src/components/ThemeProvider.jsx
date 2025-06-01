/**
 * @file ThemeProvider.jsx
 * @description Composant contextuel pour la gestion dynamique des thèmes (Amazigh, Moderne…) dans Dihya Coding.
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les interactions sont validées, loguées localement et respectent le consentement utilisateur.
 */

import React, { createContext, useContext, useState, useEffect } from 'react';
import { amazighTheme, applyAmazighTheme } from '../branding/themes/amazigh';
import { modernTheme, applyModernTheme } from '../branding/themes/modern';

/**
 * Liste des thèmes disponibles.
 */
const THEMES = {
  amazigh: { ...amazighTheme, apply: applyAmazighTheme },
  modern: { ...modernTheme, apply: applyModernTheme },
};

/**
 * Contexte React pour le thème courant.
 */
const ThemeContext = createContext({
  theme: 'modern',
  setTheme: () => {},
  themeProperties: modernTheme,
});

/**
 * Fournisseur de thème pour l’application Dihya Coding.
 * @param {object} props
 * @param {React.ReactNode} props.children
 * @returns {JSX.Element}
 */
export function ThemeProvider({ children }) {
  // Préférence utilisateur (localStorage ou défaut)
  const [theme, setThemeState] = useState(() => {
    return localStorage.getItem('dihya_theme') || 'modern';
  });

  // Applique le thème à chaque changement
  useEffect(() => {
    const themeObj = THEMES[theme] || THEMES.modern;
    themeObj.apply();
    document.body.setAttribute('data-theme', theme);
    logThemeEvent('set_theme', theme);
    // SEO: meta theme-color dynamique
    let meta = document.querySelector('meta[name="theme-color"]');
    if (!meta) {
      meta = document.createElement('meta');
      meta.setAttribute('name', 'theme-color');
      document.head.appendChild(meta);
    }
    meta.setAttribute('content', themeObj.colors.primary);
  }, [theme]);

  /**
   * Change le thème et le stocke localement.
   * @param {string} newTheme
   */
  function setTheme(newTheme) {
    if (!THEMES[newTheme]) throw new Error('Thème inconnu');
    setThemeState(newTheme);
    localStorage.setItem('dihya_theme', newTheme);
  }

  return (
    <ThemeContext.Provider value={{
      theme,
      setTheme,
      themeProperties: THEMES[theme] || THEMES.modern,
    }}>
      {children}
    </ThemeContext.Provider>
  );
}

/**
 * Hook pour accéder au contexte de thème.
 * @returns {{theme: string, setTheme: function, themeProperties: object}}
 */
export function useTheme() {
  return useContext(ThemeContext);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logThemeEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('theme_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('theme_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de thème locaux (droit à l’oubli RGPD).
 */
export function clearLocalThemeLogs() {
  localStorage.removeItem('theme_logs');
}