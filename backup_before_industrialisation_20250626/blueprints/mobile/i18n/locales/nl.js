import { setLanguage, t } from '../../i18n';
import nl from './nl.json';

export const nlLocale = {
  ...nl,
  setLanguage,
  t,
  code: 'nl',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'NL',
    label: 'Nederlands',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default nlLocale;
