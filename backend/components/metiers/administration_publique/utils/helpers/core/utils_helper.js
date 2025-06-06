// utils_helper.js - Fonctions utilitaires avancées pour Threed (JS)

module.exports = {
  formatDate: (date) => new Date(date).toISOString(),
  isObject: (obj) => obj && typeof obj === 'object' && !Array.isArray(obj),
  deepClone: (obj) => JSON.parse(JSON.stringify(obj))
};
