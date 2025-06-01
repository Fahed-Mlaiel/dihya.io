// Template für Validatoren

/**
 * Validiert eine Eingabe.
 * @param {string} input
 * @returns {boolean}
 */
function validateInput(input) {
  return typeof input === 'string' && input.length > 0;
}

module.exports = { validateInput };
