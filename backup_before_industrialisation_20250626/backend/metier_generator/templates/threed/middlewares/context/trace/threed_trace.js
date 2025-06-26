// Middleware de traçabilité pour le module threed (Node.js)
function threedTrace(req, res, next) {
  req.context = req.context || {};
  req.context.traceId = req.traceId || null;
  next();
}

module.exports = threedTrace;
