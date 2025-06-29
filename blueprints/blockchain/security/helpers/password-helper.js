// Helper pour la gestion des mots de passe (hash, validation)
const bcrypt = require('bcryptjs');

module.exports = {
  async hashPassword(password) {
    return await bcrypt.hash(password, 12);
  },
  async comparePassword(password, hash) {
    return await bcrypt.compare(password, hash);
  },
  validatePassword(password, policy = { minLength: 12, requireNumbers: true, requireSpecial: true }) {
    if (password.length < policy.minLength) return false;
    if (policy.requireNumbers && !/\d/.test(password)) return false;
    if (policy.requireSpecial && !/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(password)) return false;
    return true;
  }
};
