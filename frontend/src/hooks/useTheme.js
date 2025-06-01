/**
 * @file useTheme.js
 * @description Hook React pour la gestion du thème (clair/sombre, accessibilité, SEO) dans Dihya Coding.
 * Garantit design moderne, accessibilité, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import { useState, useEffect, useCallback } from 'react';

/**
 * Hook pour gérer le thème de l’application (clair/sombre) avec support RGPD et auditabilité.
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {[string, function, function]} [theme, toggleTheme, setTheme]
 */
export function useTheme(options = {}) {
  const defaultTheme = getInitialTheme();
  const [theme, setThemeState] = useState(defaultTheme);

  // Applique le thème au body et log l’événement
  useEffect(() => {
    document.body.setAttribute('data-theme', theme);
    if (options.log !== false && hasConsent()) {
      logThemeEvent('theme_change', { theme });
    }
    // SEO: Met à jour la meta color-scheme
    updateColorSchemeMeta(theme);
  }, [theme, options.log]);

  /**
   * Change le thème (clair/sombre).
   * @param {string} newTheme
   */
  const setTheme = useCallback((newTheme) => {
    if (!hasConsent()) return;
    if (['light', 'dark'].includes(newTheme)) {
      setThemeState(newTheme);
      window.localStorage.setItem('theme', newTheme);
      if (options.log !== false) {
        logThemeEvent('theme_set', { theme: newTheme });
      }
    }
  }, [options.log]);

  /**
   * Bascule entre les thèmes clair et sombre.
   */
  const toggleTheme = useCallback(() => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  }, [theme, setTheme]);

  return [theme, toggleTheme, setTheme];
}

/**
 * Récupère le thème initial (localStorage, media query ou 'light').
 * @returns {string}
 */
function getInitialTheme() {
  if (typeof window !== 'undefined') {
    const stored = window.localStorage.getItem('theme');
    if (stored) return stored;
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
  }
  return 'light';
}

/**
 * Met à jour la meta color-scheme pour le SEO et l’accessibilité.
 * @param {string} theme
 */
function updateColorSchemeMeta(theme) {
  if (typeof document === 'undefined') return;
  let meta = document.querySelector('meta[name="color-scheme"]');
  if (!meta) {
    meta = document.createElement('meta');
    meta.setAttribute('name', 'color-scheme');
    document.head.appendChild(meta);
  }
  meta.setAttribute('content', theme === 'dark' ? 'dark light' : 'light dark');
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('theme_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logThemeEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('theme_hook_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('theme_hook_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs du hook thème (droit à l’oubli RGPD).
 */
export function clearLocalThemeHookLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('theme_hook_logs');
  }
}