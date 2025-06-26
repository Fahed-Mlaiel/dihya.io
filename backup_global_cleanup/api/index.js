// index.js ultra avancé pour le domaine API (Node.js)
// Point d'entrée centralisé pour toutes les routes, générateurs et middlewares API

const assetRoutes = require('./routes/asset_routes');
// Ajoutez ici d'autres routes ou modules API à exposer

// Exemple d'auto-discovery pour les générateurs (si besoin)
// const backendApi = require('./generators/backendApi');

module.exports = {
  assetRoutes,
  // backendApi,
  // Ajoutez d'autres exports ici selon l'évolution du socle
};

/**
 * Exemple d'utilisation :
 * const { assetRoutes } = require('./api');
 * app.use('/api/assets', assetRoutes);
 */
