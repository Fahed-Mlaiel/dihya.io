import { setLanguage, t } from '../../i18n';
import ber from './ber.json';

export const berLocale = {
  ...ber,
  setLanguage,
  t,
  code: 'ber',
  direction: 'ltr',
  fallback: 'fr',
  meta: {
    region: 'BER',
    label: 'ⴰⵎⴰⵣⵉⵖ',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default berLocale;

module.exports = { ber };
