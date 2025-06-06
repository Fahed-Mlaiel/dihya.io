// Point d'entrée du module controllers

const ThreedController = require('./threed_controller');
// Exporte explicitement les méthodes du contrôleur Threed
module.exports = {
  create: ThreedController.create,
  delete: ThreedController.delete,
  getById: ThreedController.getById,
  update: ThreedController.update,
  // Ajouter ici d’autres contrôleurs ou helpers si besoin
};
