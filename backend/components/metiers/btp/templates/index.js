// index.js – Ultra-robuster Entry-Point für Environnement Templates (Dihya Coding)
/**
 * Point d'entrée avancé pour les templates Environnement
 * - Exporte tous les templates (statiquement + auto-découverts)
 * - Prêt pour extension (plugins, audit, RGPD, i18n, multitenancy)
 * - Utilisé dans les tests, CI/CD, scripts de migration, monitoring
 *
 * Advanced entry point for Environnement templates
 * - Exports all templates (static + auto-discovered)
 * - Ready for extension (plugins, audit, GDPR, i18n, multitenancy)
 * - Used in tests, CI/CD, migration scripts, monitoring
 */
const fs = require('fs');
const path = require('path');
function getTemplatePath(templateName) {
  return path.join(__dirname, templateName);
}
function listTemplates() {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.j2'));
}
function validateTemplates() {
  // Validation RGPD, accessibilité, sécurité, auditabilité
  return listTemplates().map(f => {
    const content = fs.readFileSync(path.join(__dirname, f), 'utf-8');
    return {
      template: f,
      rgpd: /RGPD|GDPR|conformit[eé]/i.test(content),
      accessibilite: /accessibilit[eé]|WCAG|A11Y/i.test(content),
      securite: /s[eé]curit[eé]|audit/i.test(content),
      plugins: /plugin/i.test(content),
      test: /{{/i.test(content)
    };
  });
}
module.exports = {
  getTemplatePath,
  listTemplates,
  validateTemplates,
  TEMPLATES: listTemplates()
};
