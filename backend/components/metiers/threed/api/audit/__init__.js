// Point d'entrée du module audit

const { auditEntity } = require('./audit');
// Exporte les helpers, runners et hooks d’audit
module.exports = {
  auditEntity,
  // Ajouter ici d’autres helpers/runners/hooks si besoin
};
