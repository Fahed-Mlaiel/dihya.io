// index.js - Design System Dihya Coding
/**
 * @fileoverview Design system, accessibilité, thèmes, documentation intégrée, multilingue.
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */

export const COLORS = {
  primary: '#0057b8',
  secondary: '#ffb300',
  background: '#f5f5f5',
  text: '#222',
  error: '#d32f2f',
  success: '#388e3c',
};

export const FONTS = {
  main: 'Inter, Arial, sans-serif',
  code: 'Fira Mono, monospace',
};

export const THEMES = {
  light: {
    background: COLORS.background,
    text: COLORS.text,
    primary: COLORS.primary,
    secondary: COLORS.secondary,
  },
  dark: {
    background: '#222',
    text: '#f5f5f5',
    primary: COLORS.primary,
    secondary: COLORS.secondary,
  },
};
