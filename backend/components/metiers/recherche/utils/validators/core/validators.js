// validators.js – Validateurs avancés pour Recherche (Node.js)
function isValidModel(data) {
  if (!data || typeof data !== 'object') return false;
  if (!data.nom) return false;
  if (!['actif', 'inactif', 'archive', undefined, null].includes(data.statut)) return false;
  return true;
}

function validateRequired(val) {
  return val !== undefined && val !== null && val !== '';
}

module.exports = {
  isValidModel,
  validateRequired
};
