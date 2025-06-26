import { setLanguage, t } from '../../i18n';
import sv from './sv.json';

export const svLocale = {
  ...sv,
  setLanguage,
  t,
  code: 'sv',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'SE',
    label: 'Svenska',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default svLocale;
