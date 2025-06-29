import { setLanguage, t } from '../../i18n';
import fr from './fr.json';

export const frLocale = {
  ...fr,
  setLanguage,
  t,
  code: 'fr',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'FR',
    label: 'Français',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default frLocale;
