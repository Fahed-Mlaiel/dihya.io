import { setLanguage, t } from '../../i18n';
import no from './no.json';

export const noLocale = {
  ...no,
  setLanguage,
  t,
  code: 'no',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'NO',
    label: 'Norsk',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default noLocale;
