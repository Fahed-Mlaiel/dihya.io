// Middleware de pagination API threed (Node.js) - Ultra avancé
// Gère la validation, les bornes, la doc, l'intégration métier
// Utilisation : app.use(require('./pagination'));

function paginationMiddleware(req, res, next) {
  let page = parseInt(req.query.page || '1', 10);
  let size = parseInt(req.query.size || '10', 10);
  if (isNaN(page) || page < 1) page = 1;
  if (isNaN(size) || size < 1 || size > 100) size = 10;
  req.pagination = { page, size };
  // Expose pour la logique métier
  req.businessContext = req.businessContext || {};
  req.businessContext.pagination = req.pagination;
  next();
}

module.exports = paginationMiddleware;

// Exemple d'intégration :
// app.use(require('./pagination'));
// Dans un contrôleur : req.pagination.page, req.pagination.size
