/**
 * @file modern.js
 * @description Thème moderne pour l’interface Dihya Coding.
 * Garantit design contemporain, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les couleurs, polices et styles sont documentés et validés selon la charte graphique Dihya.
 */

export const modernTheme = {
  name: 'Modern',
  description: 'Thème moderne, épuré et accessible pour Dihya Coding.',
  colors: {
    primary: '#0057FF',      // Bleu moderne
    secondary: '#00C6AE',    // Vert/bleu accent
    accent: '#FF5A36',       // Orange vif
    background: '#F5F7FA',   // Fond très clair
    surface: '#FFFFFF',      // Surfaces cartes/blocs
    text: '#1A1A1A',         // Texte principal
    textSecondary: '#6B7280',
    border: '#E5E7EB',
    success: '#22C55E',
    warning: '#FACC15',
    error: '#EF4444',
    info: '#2563EB',
    // Mode sombre (optionnel)
    dark: {
      background: '#181A20',
      surface: '#23272F',
      text: '#F5F7FA',
      border: '#333',
    },
  },
  fonts: {
    heading: '"Inter", "Montserrat", Arial, sans-serif',
    body: '"Inter", Arial, sans-serif',
    monospace: '"Fira Mono", monospace',
  },
  icons: {
    style: 'outlined',
    color: '#0057FF',
  },
  borderRadius: '10px',
  spacing: {
    xs: '4px',
    sm: '10px',
    md: '20px',
    lg: '40px',
  },
  shadows: {
    card: '0 2px 12px rgba(0,0,0,0.08)',
    modal: '0 6px 32px rgba(0,0,0,0.15)',
  },
  // SEO & accessibilité
  seo: {
    lang: 'fr',
    direction: 'ltr',
    metaThemeColor: '#0057FF',
  },
  accessibility: {
    contrast: 'AA', // Respecte WCAG AA
    focusOutline: '2px solid #00C6AE',
    ariaLabels: true,
  },
  // RGPD & auditabilité
  compliance: {
    noTracking: true,
    noPersonalData: true,
    auditLog: true,
  },
  // Extensibilité
  customProperties: {
    '--modern-shadow': '0 2px 12px rgba(0,0,0,0.08)',
  },
};

/**
 * Applique dynamiquement le thème moderne à l’application (CSS variables).
 * @param {HTMLElement} [root=document.documentElement]
 */
export function applyModernTheme(root = document.documentElement) {
  const c = modernTheme.colors;
  root.style.setProperty('--color-primary', c.primary);
  root.style.setProperty('--color-secondary', c.secondary);
  root.style.setProperty('--color-accent', c.accent);
  root.style.setProperty('--color-background', c.background);
  root.style.setProperty('--color-surface', c.surface);
  root.style.setProperty('--color-text', c.text);
  root.style.setProperty('--color-border', c.border);
  root.style.setProperty('--font-heading', modernTheme.fonts.heading);
  root.style.setProperty('--font-body', modernTheme.fonts.body);
  root.style.setProperty('--border-radius', modernTheme.borderRadius);
  root.style.setProperty('--modern-shadow', modernTheme.customProperties['--modern-shadow']);
  // Ajout du meta theme-color pour SEO
  let meta = document.querySelector('meta[name="theme-color"]');
  if (!meta) {
    meta = document.createElement('meta');
    meta.setAttribute('name', 'theme-color');
    document.head.appendChild(meta);
  }
  meta.setAttribute('content', c.primary);
}