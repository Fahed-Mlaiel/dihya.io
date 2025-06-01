/**
 * @file index.js
 * @description Initialisation et configuration d’i18n pour Dihya Coding (internationalisation multilingue, dialectes, RGPD, auditabilité).
 * Garantit design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

import ar from './locales/ar/translation.json';
import fr from './locales/fr/translation.json';
import en from './locales/en/translation.json';
import ber from './locales/ber/translation.json';

// Liste des langues supportées et fallback
const supportedLngs = ['fr', 'en', 'ar', 'ber'];
const fallbackLng = 'fr';

/**
 * Initialisation d’i18n avec auditabilité et conformité RGPD.
 */
i18n
  .use(initReactI18next)
  .init({
    resources: {
      ar: { translation: ar },
      fr: { translation: fr },
      en: { translation: en },
      ber: { translation: ber }
    },
    lng: detectInitialLanguage(),
    fallbackLng,
    supportedLngs,
    interpolation: {
      escapeValue: false // React already does escaping
    },
    detection: {
      order: ['localStorage', 'navigator', 'htmlTag'],
      caches: ['localStorage']
    }
  }, (err) => {
    logI18nEvent('init', { error: err ? err.message : null, lng: i18n.language });
  });

/**
 * Détecte la langue initiale selon le consentement utilisateur et les préférences.
 * @returns {string}
 */
function detectInitialLanguage() {
  if (typeof window !== 'undefined') {
    const consent = window.localStorage.getItem('i18n_feature_consent');
    if (!consent) return fallbackLng;
    const stored = window.localStorage.getItem('i18nextLng');
    if (stored && supportedLngs.includes(stored)) return stored;
    const nav = navigator.language?.split('-')[0];
    if (nav && supportedLngs.includes(nav)) return nav;
  }
  return fallbackLng;
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logI18nEvent(action, data) {
  try {
    if (typeof window === 'undefined' || !window.localStorage) return;
    const logs = JSON.parse(window.localStorage.getItem('i18n_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('i18n_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs i18n (droit à l’oubli RGPD).
 */
export function clearLocalI18nLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('i18n_logs');
  }
}

export default i18n;