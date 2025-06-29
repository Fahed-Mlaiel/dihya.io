import { setLanguage, t } from '../../i18n';
import tac from './tac.json';

export const tacLocale = {
  ...tac,
  setLanguage,
  t,
  code: 'tac',
  direction: 'ltr',
  fallback: 'ber',
  meta: {
    region: 'TAC',
    label: 'Tachelhit',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default tacLocale;

module.exports = { tac };
