// Middleware de gestion de session pour le module threed (Node.js)
function threedSession(req, res, next) {
  req.context = req.context || {};
  req.context.session = req.session || {};
  next();
}

module.exports = threedSession;
