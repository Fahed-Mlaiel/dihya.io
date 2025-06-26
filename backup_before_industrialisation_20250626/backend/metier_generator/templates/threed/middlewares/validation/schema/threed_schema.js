// Middleware de validation de schéma pour le module threed (Node.js)
function threedSchema(req, res, next) {
  if (req.schema && typeof req.schema.validate === 'function') {
    req.schema.validate(req.body || {});
  }
  next();
}

module.exports = threedSchema;
