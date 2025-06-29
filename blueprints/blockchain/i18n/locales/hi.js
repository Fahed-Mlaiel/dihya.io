import { setLanguage, t } from '../../i18n';
import hi from './hi.json';

export const hiLocale = {
  ...hi,
  setLanguage,
  t,
  code: 'hi',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'IN',
    label: 'हिन्दी',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default hiLocale;
