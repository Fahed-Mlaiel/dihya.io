import { setLanguage, t } from '../../i18n';
import ja from './ja.json';

export const jaLocale = {
  ...ja,
  setLanguage,
  t,
  code: 'ja',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'JP',
    label: '日本語',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default jaLocale;
