import { setLanguage, t } from '../../i18n';
import kab from './kab.json';

export const kabLocale = {
  ...kab,
  setLanguage,
  t,
  code: 'kab',
  direction: 'ltr',
  fallback: 'fr',
  meta: {
    region: 'KAB',
    label: 'Kabyle',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default kabLocale;
