// Middleware JS – Ultra avancé
module.exports = {
  logMiddleware: () => (req, res, next) => {
    console.log('Request:', req.method, req.url);
    next();
  }
};
