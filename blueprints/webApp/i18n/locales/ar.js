import { setLanguage, t } from '../../i18n';
import ar from './ar.json';

export const arLocale = {
  ...ar,
  setLanguage,
  t,
  code: 'ar',
  direction: 'rtl',
  fallback: 'fr',
  meta: {
    region: 'AR',
    label: 'العربية',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default arLocale;
