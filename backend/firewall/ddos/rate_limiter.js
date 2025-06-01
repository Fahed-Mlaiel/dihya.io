// rate_limiter.js – Middleware rate limiting (Node.js, Dihya)
const rateLimit = require('express-rate-limit');

module.exports = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 100, // 100 requêtes/minute
  message: 'Trop de requêtes, réessayez plus tard.'
});
