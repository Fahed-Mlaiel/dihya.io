// Fonctions utilitaires pour la gestion des templates JSON

function validateJsonTemplate(template) {
  // Validation basique
  return typeof template === 'object';
}

module.exports = { validateJsonTemplate };
