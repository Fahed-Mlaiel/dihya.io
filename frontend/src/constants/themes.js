/**
 * @file themes.js
 * @description Constantes des thèmes graphiques disponibles pour Dihya Coding.
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Aucun secret, donnée personnelle ou sensible n’est stocké ici.
 */

/**
 * Liste des thèmes graphiques disponibles.
 * @readonly
 * @type {Array<{code: string, label: string, description: string, emoji: string}>}
 */
export const THEMES_LIST = [
  {
    code: 'modern',
    label: 'Moderne',
    description: 'Thème moderne, épuré et accessible pour Dihya Coding.',
    emoji: '✨',
  },
  {
    code: 'amazigh',
    label: 'Amazigh',
    description: 'Thème inspiré de la culture amazighe, moderne et conforme.',
    emoji: 'ⵣ',
  },
];

/**
 * Récupère la description d’un thème par son code.
 * @param {string} code
 * @returns {string|null}
 */
export function getThemeDescription(code) {
  const theme = THEMES_LIST.find(t => t.code === code);
  return theme ? theme.description : null;
}

/**
 * Vérifie si un thème est supporté.
 * @param {string} code
 * @returns {boolean}
 */
export function isValidTheme(code) {
  return THEMES_LIST.some(t => t.code === code);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} themeCode
 */
export function logThemeConstantEvent(action, themeCode) {
  try {
    const logs = JSON.parse(localStorage.getItem('theme_constant_logs') || '[]');
    logs.push({
      action,
      themeCode,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('theme_constant_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de thèmes locaux (droit à l’oubli RGPD).
 */
export function clearLocalThemeConstantLogs() {
  localStorage.removeItem('theme_constant_logs');
}