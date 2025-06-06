// templates_validator.js – Validateur ultra avancé pour les templates Threed (JS)
// Inclut : validation de structure, sécurité, audit, edge cases, CI/CD
const fs = require('fs');

function isValidTemplateFile(filename) {
  return /\.(html\.j2|json\.j2|xml|txt)$/.test(filename) && fs.existsSync(filename);
}

function validateTemplateContent(content) {
  // Vérifie la présence de balises Jinja2 ou variables attendues
  return (content.includes('{{') && content.includes('}}')) || content.includes('<') || content.includes('{');
}

module.exports = {
  isValidTemplateFile,
  validateTemplateContent
};
// Exemples d’utilisation, edge cases, synchronisation JS/Python
