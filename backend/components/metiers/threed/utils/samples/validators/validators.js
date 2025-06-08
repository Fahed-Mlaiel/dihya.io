// validators.js - Exemple métier principal validators
function validateData(data) {
  return data && typeof data === 'object' && Object.keys(data).length > 0;
}
module.exports = validateData;
