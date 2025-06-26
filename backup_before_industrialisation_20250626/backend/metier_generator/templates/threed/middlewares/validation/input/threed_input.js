// Middleware de validation d’entrée pour le module threed (Node.js)
function threedInput(req, res, next) {
  if (!req.body) {
    return res.status(400).json({ error: 'Aucune donnée fournie' });
  }
  next();
}

module.exports = threedInput;
