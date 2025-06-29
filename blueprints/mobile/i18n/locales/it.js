import { setLanguage, t } from '../../i18n';
import it from './it.json';

export const itLocale = {
  ...it,
  setLanguage,
  t,
  code: 'it',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'IT',
    label: 'Italiano',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default itLocale;
