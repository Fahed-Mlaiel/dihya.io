// Middleware d’authentification avancée pour le module threed (Node.js)
function threedAuth(req, res, next) {
  if (!req.user || !req.user.isAuthenticated) {
    return res.status(401).json({ error: 'Authentification requise' });
  }
  next();
}

module.exports = threedAuth;
