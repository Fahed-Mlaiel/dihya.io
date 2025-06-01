/**
 * @file Branding.js
 * @description Composant centralisé pour la gestion du branding (logo, couleurs, thèmes, polices) de Dihya Coding.
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les propriétés sont validées et documentées selon la charte graphique Dihya.
 */

import React from 'react';
import { amazighTheme, applyAmazighTheme } from './themes/amazigh';
import { modernTheme, applyModernTheme } from './themes/modern';
import logoDihya from './assets/logos/dihya-logo.svg';

/**
 * Applique dynamiquement le thème choisi à l’application.
 * @param {'amazigh'|'modern'} themeName
 */
export function setBrandingTheme(themeName) {
  if (themeName === 'amazigh') {
    applyAmazighTheme();
  } else if (themeName === 'modern') {
    applyModernTheme();
  } else {
    throw new Error('Thème inconnu');
  }
  logBrandingEvent('set_theme', themeName);
}

/**
 * Composant React pour afficher le logo Dihya Coding avec accessibilité et SEO.
 * @param {object} props
 * @param {string} [props.alt] - Texte alternatif pour accessibilité/SEO
 * @param {string} [props['aria-label']] - Label ARIA pour lecteurs d’écran
 * @param {number|string} [props.width] - Largeur du logo
 * @param {number|string} [props.height] - Hauteur du logo
 * @returns {JSX.Element}
 */
export function DihyaLogo({
  alt = 'Logo Dihya Coding',
  'aria-label': ariaLabel = 'Logo Dihya Coding',
  width = 48,
  height = 48,
  ...rest
}) {
  return (
    <img
      src={logoDihya}
      alt={alt}
      aria-label={ariaLabel}
      width={width}
      height={height}
      loading="lazy"
      style={{ display: 'inline-block', verticalAlign: 'middle' }}
      {...rest}
    />
  );
}

/**
 * Récupère les propriétés du thème courant.
 * @param {'amazigh'|'modern'} themeName
 * @returns {object} Propriétés du thème
 */
export function getThemeProperties(themeName) {
  if (themeName === 'amazigh') return amazighTheme;
  if (themeName === 'modern') return modernTheme;
  throw new Error('Thème inconnu');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logBrandingEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('branding_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('branding_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de branding locaux (droit à l’oubli RGPD).
 */
export function clearLocalBrandingLogs() {
  localStorage.removeItem('branding_logs');
}