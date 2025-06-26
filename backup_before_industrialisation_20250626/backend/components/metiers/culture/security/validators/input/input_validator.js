// input_validator.js – Validation des entrées

function validateInput(data) {
  if (typeof data !== 'object' || Array.isArray(data)) throw new Error('Entrée invalide : doit être un objet');
  if (!('user' in data) || !('action' in data)) throw new Error('Entrée invalide : champs requis manquants');
  return true;
}

module.exports = { validateInput };
