// module_utils.js – Fonctions utilitaires JS pour modules patterns
module.exports = {
  capitalize: (str) => str.charAt(0).toUpperCase() + str.slice(1),
  slugify: (str) => str.toLowerCase().replace(/\s+/g, '-'),
};
