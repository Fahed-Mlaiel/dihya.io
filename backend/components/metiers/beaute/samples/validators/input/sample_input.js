// Exemple avancé de validation d’input (Node.js)

module.exports = function validateInput(input) {
  return typeof input === 'string' && input.length > 0;
};
