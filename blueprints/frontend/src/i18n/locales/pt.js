import { setLanguage, t } from '../../i18n';
import pt from './pt.json';

export const ptLocale = {
  ...pt,
  setLanguage,
  t,
  code: 'pt',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'PT',
    label: 'Português',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default ptLocale;
