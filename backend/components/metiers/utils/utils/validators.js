// validators.js – Validateurs avancés pour Environnement (Node.js)
module.exports = function validateEnvironnement(data) {
  if (!data.nom) throw new Error('Nom requis');
  if (!['actif', 'inactif', 'archivé', undefined, null].includes(data.statut)) {
    throw new Error('Statut invalide');
  }
  return true;
};
