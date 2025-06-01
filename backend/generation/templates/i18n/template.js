/**
 * I18N Template
 * @module i18n/template
 * @description Internationalisation dynamique multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
 * @author Dihya Team
 * @license MIT
 */

'use strict';

const resources = {
  fr: { hello: 'Bonjour', bye: 'Au revoir' },
  en: { hello: 'Hello', bye: 'Goodbye' },
  ar: { hello: 'مرحبا', bye: 'مع السلامة' },
  de: { hello: 'Hallo', bye: 'Tschüss' },
  zh: { hello: '你好', bye: '再见' },
  ja: { hello: 'こんにちは', bye: 'さようなら' },
  ko: { hello: '안녕하세요', bye: '안녕히 가세요' },
  nl: { hello: 'Hallo', bye: 'Tot ziens' },
  he: { hello: 'שלום', bye: 'להתראות' },
  fa: { hello: 'سلام', bye: 'خداحافظ' },
  hi: { hello: 'नमस्ते', bye: 'अलविदा' },
  es: { hello: 'Hola', bye: 'Adiós' }
};

/**
 * Charge les ressources pour une langue donnée.
 * @param {string} lang - Code langue
 * @returns {Object} Ressources localisées
 */
function load(lang) {
  return resources[lang] || resources['en'];
}

module.exports = { load };
