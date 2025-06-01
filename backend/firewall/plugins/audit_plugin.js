// audit_plugin.js – Plugin d’audit sécurité (Dihya)
module.exports = function auditPlugin(req, res, next) {
  console.log('[AUDIT]', new Date().toISOString(), req.method, req.url, req.user ? req.user.id : null);
  next();
};
