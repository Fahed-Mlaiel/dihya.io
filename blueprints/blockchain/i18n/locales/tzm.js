import { setLanguage, t } from '../../i18n';
import tzm from './tzm.json';

export const tzmLocale = {
  ...tzm,
  setLanguage,
  t,
  code: 'tzm',
  direction: 'ltr',
  fallback: 'fr',
  meta: {
    region: 'TZM',
    label: 'ⵜⴰⵎⴰⵣⵉⵖⵜ',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default tzmLocale;

module.exports = { tzm };
