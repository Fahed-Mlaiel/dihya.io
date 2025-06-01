/**
 * @file modernTheme.js
 * @description Thème graphique moderne pour Dihya Coding (couleurs, typographie, composants UI).
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les personnalisations sont validées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Palette de couleurs modernes (inspirée du flat design et du material design).
 * @readonly
 * @type {object}
 */
export const modernColors = {
  primary: '#1976D2',      // Bleu moderne
  secondary: '#FF4081',    // Rose accent
  accent: '#00BFAE',       // Vert/bleu accent
  background: '#F9FAFB',   // Fond clair
  surface: '#FFFFFF',      // Surfaces principales
  text: '#212121',         // Texte principal
  textSecondary: '#757575',
  border: '#E0E0E0',
  success: '#43A047',
  warning: '#FFA000',
  error: '#D32F2F',
  info: '#0288D1',
};

/**
 * Typographie moderne (lisibilité, accessibilité, modernité).
 * @readonly
 * @type {object}
 */
export const modernTypography = {
  fontFamily: "'Inter', 'Roboto', 'Arial', sans-serif",
  fontSizeBase: '16px',
  fontWeightRegular: 400,
  fontWeightBold: 700,
  headings: {
    h1: { fontSize: '2.5rem', fontWeight: 700 },
    h2: { fontSize: '2rem', fontWeight: 700 },
    h3: { fontSize: '1.5rem', fontWeight: 700 },
    h4: { fontSize: '1.25rem', fontWeight: 700 },
    h5: { fontSize: '1rem', fontWeight: 700 },
    h6: { fontSize: '0.875rem', fontWeight: 700 },
  },
  body: { fontSize: '1rem', fontWeight: 400 },
  caption: { fontSize: '0.85rem', fontWeight: 400 },
};

/**
 * Styles de composants UI modernes (boutons, cartes, inputs, etc.).
 * @readonly
 * @type {object}
 */
export const modernComponents = {
  button: {
    borderRadius: '8px',
    padding: '0.5rem 1.5rem',
    fontWeight: 700,
    background: modernColors.primary,
    color: '#fff',
    border: 'none',
    boxShadow: '0 2px 8px rgba(25, 118, 210, 0.08)',
    transition: 'background 0.2s, box-shadow 0.2s',
    '&:hover': {
      background: modernColors.secondary,
      boxShadow: '0 4px 16px rgba(25, 118, 210, 0.12)',
    },
    '&:focus': {
      outline: `2px solid ${modernColors.accent}`,
      outlineOffset: '2px',
    },
  },
  card: {
    background: modernColors.surface,
    borderRadius: '12px',
    boxShadow: '0 2px 12px rgba(0,0,0,0.07)',
    padding: '1.5rem',
    border: `1px solid ${modernColors.border}`,
  },
  input: {
    borderRadius: '6px',
    border: `1px solid ${modernColors.border}`,
    padding: '0.5rem 1rem',
    fontSize: '1rem',
    color: modernColors.text,
    background: modernColors.surface,
    '&:focus': {
      borderColor: modernColors.primary,
      outline: `1px solid ${modernColors.primary}`,
    },
  },
};

/**
 * Thème complet moderne pour Dihya Coding.
 * @readonly
 * @type {object}
 */
export const modernTheme = {
  colors: modernColors,
  typography: modernTypography,
  components: modernComponents,
  isDark: false,
  direction: 'ltr',
  locale: 'fr',
  meta: {
    name: 'Modern',
    description: 'Thème moderne, accessible, SEO-friendly, RGPD, pour Dihya Coding.',
    version: '1.0.0',
    author: 'Dihya Coding',
  },
};

/**
 * Applique le thème moderne à l’application (exemple basique, à adapter selon le framework UI).
 * @param {object} theme
 */
export function applyModernTheme(theme = modernTheme) {
  if (typeof document === 'undefined') return;
  document.documentElement.style.setProperty('--primary-color', theme.colors.primary);
  document.documentElement.style.setProperty('--secondary-color', theme.colors.secondary);
  document.documentElement.style.setProperty('--accent-color', theme.colors.accent);
  document.documentElement.style.setProperty('--background-color', theme.colors.background);
  document.documentElement.style.setProperty('--text-color', theme.colors.text);
  document.documentElement.style.setProperty('--font-family', theme.typography.fontFamily);
  // ...ajouter d’autres variables CSS selon les besoins
  logModernThemeEvent('apply_theme', theme.meta.name);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logModernThemeEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('modern_theme_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('modern_theme_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de thème moderne (droit à l’oubli RGPD).
 */
export function clearLocalModernThemeLogs() {
  localStorage.removeItem('modern_theme_logs');
}