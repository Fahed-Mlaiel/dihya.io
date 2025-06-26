// Middleware d’audit d’accès pour le module threed (Node.js)
function threedAudit(req, res, next) {
  console.log(`[AUDIT] ${req.user ? req.user.id : 'anonyme'} accède à ${req.url}`);
  next();
}

module.exports = threedAudit;
