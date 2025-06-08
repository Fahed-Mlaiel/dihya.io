// Middleware imbriqué JS – Ultra avancé
module.exports = {
  logNestedMiddleware: () => (req, res, next) => {
    console.log('Nested Middleware:', req.method, req.url);
    next();
  }
};
