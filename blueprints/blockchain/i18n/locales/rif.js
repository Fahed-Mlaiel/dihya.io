import { setLanguage, t } from '../../i18n';
import rif from './rif.json';

export const rifLocale = {
  ...rif,
  setLanguage,
  t,
  code: 'rif',
  direction: 'ltr',
  fallback: 'ber',
  meta: {
    region: 'RIF',
    label: 'Rifain',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default rifLocale;

module.exports = { rif };
