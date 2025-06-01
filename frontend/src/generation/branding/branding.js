// branding.js - Génération de branding (frontend)
/**
 * @fileoverview Génération de branding personnalisable, multilingue, sécurité, documentation intégrée.
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */
import { SUPPORTED_LANGUAGES } from '../../constants/constants';

export function generateBranding({ name, language = 'fr' }) {
  if (!SUPPORTED_LANGUAGES.includes(language)) throw new Error('Langue non supportée');
  return {
    slogan: `${name} – ${language === 'fr' ? 'Innovation' : 'Innovation'}`,
    logo: `/assets/branding/${name}.svg`,
    color: '#0057b8',
  };
}
