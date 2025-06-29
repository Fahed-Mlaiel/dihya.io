// helper_security.js – Helpers de sécurité (JS)
const crypto = require('crypto');
function hashPassword(password) {
  return crypto.createHash('sha256').update(password).digest('hex');
}
module.exports = { hashPassword };
