import { setLanguage, t } from '../../i18n';
import zh from './zh.json';

export const zhLocale = {
  ...zh,
  setLanguage,
  t,
  code: 'zh',
  direction: 'ltr',
  fallback: 'en',
  meta: {
    region: 'CN',
    label: '中文',
    updated: '2025-06-19',
    audit: '100% conforme',
  }
};

export default zhLocale;
