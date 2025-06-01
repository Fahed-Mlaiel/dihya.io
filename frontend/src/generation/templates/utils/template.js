// Template utilitaire pour la génération de projets IA, VR, AR, etc.
// Sécurité, i18n, audit, conformité RGPD, extensibilité plugins.
// SPDX-License-Identifier: MIT

/**
 * Fonction de log sécurisé et structuré (audit, RGPD)
 * @param {string} event - Nom de l'événement
 * @param {object} [data] - Données associées (anonymisées)
 * @param {string} [level] - Niveau ('info', 'warn', 'error')
 */
export function secureLog(event, data = {}, level = 'info') {
  const msg = `[AUDIT] ${event} | ${JSON.stringify(data)}`;
  if (level === 'error') {
    console.error(msg);
  } else if (level === 'warn') {
    console.warn(msg);
  } else {
    console.info(msg);
  }
}

/**
 * Récupère les chaînes localisées (i18n dynamique)
 * @param {string} lang - Code langue
 * @returns {object} Traductions
 */
export function getI18n(lang = 'fr') {
  const translations = {
    fr: { greeting: 'Bonjour' },
    en: { greeting: 'Hello' },
    ar: { greeting: 'مرحبا' },
    de: { greeting: 'Hallo' },
    zh: { greeting: '你好' },
    ja: { greeting: 'こんにちは' },
    ko: { greeting: '안녕하세요' },
    nl: { greeting: 'Hallo' },
    he: { greeting: 'שלום' },
    fa: { greeting: 'سلام' },
    hi: { greeting: 'नमस्ते' },
    es: { greeting: 'Hola' },
    amazigh: { greeting: 'ⴰⵣⵓⵍ' }
  };
  return translations[lang] || translations.fr;
}

/**
 * Validation d'entrée utilisateur (sécurité, RGPD)
 * @param {object} data - Données à valider
 * @param {object} schema - Schéma de validation (clé: type)
 * @returns {boolean}
 */
export function validateInput(data, schema) {
  for (const key in schema) {
    if (!(key in data) || typeof data[key] !== schema[key]) {
      return false;
    }
  }
  return true;
}
