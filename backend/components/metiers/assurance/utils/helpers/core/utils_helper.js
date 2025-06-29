// utils_helper.js - Fonctions utilitaires avancées pour Assurance (JS)

module.exports = {
  formatDate: (date) => new Date(date).toISOString(),
  isObject: (obj) => obj !== null && typeof obj === 'object' && !Array.isArray(obj),
  deepClone: (obj) => JSON.parse(JSON.stringify(obj))
};
