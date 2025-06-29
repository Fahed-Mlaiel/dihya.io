// Point d’entrée JS pour la documentation des assets de patterns
// Permet d’importer et d’exposer les guides, conventions et docs multilingues

const fr = require('./assets_doc_fr.md');
const en = require('./assets_doc_en.md');
const ar = require('./assets_doc_ar.md');
const ber = require('./assets_doc_ber.md');

module.exports = {
  fr,
  en,
  ar,
  ber
};
