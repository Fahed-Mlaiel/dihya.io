// Middleware de versioning API threed (Node.js) - Ultra avancé
// Gère la détection, la validation, la logique métier multi-version
// Utilisation : app.use(require('./versioning'));

const SUPPORTED_VERSIONS = ['1.0', '2.0'];

function versioningMiddleware(req, res, next) {
  const version = req.headers['x-api-version'] || '1.0';
  if (!SUPPORTED_VERSIONS.includes(version)) {
    return res.status(400).json({ error: 'API version not supported', supported: SUPPORTED_VERSIONS });
  }
  req.apiVersion = version;
  req.businessContext = req.businessContext || {};
  req.businessContext.apiVersion = version;
  next();
}

module.exports = versioningMiddleware;

// Exemple d'intégration :
// app.use(require('./versioning'));
// Dans un contrôleur : req.apiVersion
