// Helper pour la génération et la vérification de JWT
const jwt = require('jsonwebtoken');

module.exports = {
  signJWT(payload, secret, options = {}) {
    return jwt.sign(payload, secret, { expiresIn: '1h', ...options });
  },
  verifyJWT(token, secret) {
    try {
      return jwt.verify(token, secret);
    } catch (e) {
      return null;
    }
  }
};
