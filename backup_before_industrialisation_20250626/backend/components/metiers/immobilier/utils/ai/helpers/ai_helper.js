// ai_helper.js
// Helper IA JS pour Immobilier – exemple clé en main

/**
 * Nettoie et normalise un texte pour l'IA (suppression espaces, accents, etc.)
 * @param {string} text
 * @returns {string}
 */
function normalizeText(text) {
  if (!text) return '';
  return text
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

module.exports = { normalizeText };
