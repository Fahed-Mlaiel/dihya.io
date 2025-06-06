/* global console */
// sample_users.js – Exemple ultra avancé de génération d'utilisateurs (fixtures/core)
const { generateUser } = require('../fixtures.generator');
const { auditFixture } = require('../audit');
const { rgpdSanitize } = require('../rgpd');

function sampleUsersUltra() {
  // Génération d'un utilisateur avec audit, RGPD, accessibilité
  let user = generateUser('superadmin');
  user = rgpdSanitize(user);
  auditFixture(user, 'generate');
  console.info('Utilisateur généré:', user);
  console.log('Utilisateur ultra avancé généré avec succès.');
}

module.exports = sampleUsersUltra;
