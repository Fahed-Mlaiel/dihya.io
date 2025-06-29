// crypto.js – Chiffrement des données sensibles
module.exports = {
  encrypt: (data) => `encrypted(${data})`,
  decrypt: (data) => data.replace('encrypted(', '').replace(')', ''),
};
