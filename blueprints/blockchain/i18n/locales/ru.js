import { setLanguage, t } from '../../i18n';
import ru from './ru.json';

export const ruLocale = {
  ...ru,
  setLanguage,
  t,
  code: 'ru',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'RU',
    label: 'Русский',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default ruLocale;

module.exports = { ru };
