// validators.js – Validation des entrées, sécurité uploads
module.exports = {
  isValidEmail: (email) => /.+@.+\..+/.test(email),
  isValidFile: (file) => file && file.size < 5 * 1024 * 1024,
};
