// rgpd_validator.js – Validation conformité RGPD

function validateRGPD(data) {
  if ('personal_data' in data && !data.consent) throw new Error('Non conforme RGPD : consentement manquant');
  return true;
}

module.exports = { validateRGPD };
