import { setLanguage, t } from '../../i18n';
import en from './en.json';

export const enLocale = {
  ...en,
  setLanguage,
  t,
  code: 'en',
  direction: 'ltr',
  fallback: 'fr',
  meta: {
    region: 'EN',
    label: 'English',
    updated: '2025-06-19',
    audit: '100% compliant',
  }
};

export default enLocale;
