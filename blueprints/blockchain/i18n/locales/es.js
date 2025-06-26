import { setLanguage, t } from '../../i18n';
import es from './es.json';

export const esLocale = {
  ...es,
  setLanguage,
  t,
  code: 'es',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'ES',
    label: 'Español',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default esLocale;

module.exports = { es };
