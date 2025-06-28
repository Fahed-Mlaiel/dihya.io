// Exemple avancé de validation RGPD (Node.js)

module.exports = function validateRGPD(data) {
  return data.hasConsent === true;
};
