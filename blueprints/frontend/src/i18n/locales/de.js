import { setLanguage, t } from '../../i18n';
import de from './de.json';

export const deLocale = {
  ...de,
  setLanguage,
  t,
  code: 'de',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'DE',
    label: 'Deutsch',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default deLocale;
