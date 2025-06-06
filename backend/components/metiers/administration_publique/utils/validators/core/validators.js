// validators.js – Validateurs avancés pour Threed (Node.js)
module.exports = function validateThreed(data) {
  if (!data.name) throw new Error('Nom requis');
  if (!['active', 'inactive', 'archived', undefined, null].includes(data.status)) {
    throw new Error('Statut invalide');
  }
  return true;
};
