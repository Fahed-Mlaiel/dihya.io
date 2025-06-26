// Middleware de logging avancé pour le métier threed (Node.js)
function threedLogger(req, res, next) {
  console.log(`[THREED] ${req.method} ${req.url}`);
  next();
}

module.exports = threedLogger;
