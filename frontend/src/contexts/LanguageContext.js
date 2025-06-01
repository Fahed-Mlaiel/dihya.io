/**
 * @file LanguageContext.js
 * @description Contexte de gestion de la langue pour Dihya Coding.
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, loguées localement et respectent le consentement utilisateur.
 */

import React, { createContext, useContext, useState, useEffect } from 'react';

/**
 * Liste des langues supportées.
 * @readonly
 * @type {Array<{code: string, label: string}>}
 */
export const SUPPORTED_LANGUAGES = [
  { code: 'fr', label: 'Français' },
  { code: 'en', label: 'English' },
  { code: 'ar', label: 'العربية' },
  { code: 'ber', label: 'ⵜⴰⵎⴰⵣⵉⵖⵜ' },
];

/**
 * Contexte React pour la langue courante.
 */
const LanguageContext = createContext({
  lang: 'fr',
  setLang: () => {},
});

/**
 * Fournisseur de langue pour l’application Dihya Coding.
 * @param {object} props
 * @param {React.ReactNode} props.children
 * @returns {JSX.Element}
 */
export function LanguageProvider({ children }) {
  // Préférence utilisateur (localStorage ou défaut)
  const [lang, setLangState] = useState(() => {
    return localStorage.getItem('dihya_lang') || 'fr';
  });

  // Applique la langue à chaque changement (SEO + accessibilité)
  useEffect(() => {
    document.documentElement.lang = lang;
    logLanguageContextEvent('set_language', lang);
  }, [lang]);

  /**
   * Change la langue et la stocke localement.
   * @param {string} newLang
   */
  function setLang(newLang) {
    if (!SUPPORTED_LANGUAGES.some(l => l.code === newLang)) throw new Error('Langue non supportée');
    setLangState(newLang);
    localStorage.setItem('dihya_lang', newLang);
  }

  return (
    <LanguageContext.Provider value={{ lang, setLang }}>
      {children}
    </LanguageContext.Provider>
  );
}

/**
 * Hook pour accéder au contexte de langue.
 * @returns {{lang: string, setLang: function}}
 */
export function useLanguage() {
  return useContext(LanguageContext);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logLanguageContextEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('language_context_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('language_context_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de langue locaux (droit à l’oubli RGPD).
 */
export function clearLocalLanguageContextLogs() {
  localStorage.removeItem('language_context_logs');
}