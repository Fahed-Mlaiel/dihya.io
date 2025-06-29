// middleware.js – Middlewares sécurité, CORS, rate limiting
module.exports = {
  cors: (req, res, next) => { next(); },
  rateLimit: (req, res, next) => { next(); },
};
