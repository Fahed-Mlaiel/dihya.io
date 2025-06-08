// index.js - Point d'entrée du core sécurité 3D
// Permet l'import modulaire des modules core (policy, crypto, access_control) et des samples avancés

const policy = require('./policy');
const crypto = require('./crypto');
const accessControl = require('./access_control');
const samples = require('./samples');

module.exports = {
  policy,
  crypto,
  accessControl,
  samples
};
