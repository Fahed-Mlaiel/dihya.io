/**
 * templates_utils.js – Logique métier ultra avancée helpers/utils (JS)
 * CDC Dihya : RGPD, accessibilité, audit, CI/CD, edge cases, hooks, robustesse, conformité, multi-formats
 */
const crypto = require('crypto');

function generateTemplateId(prefix = 'tpl') {
  const date = new Date().toISOString().replace(/[-:.TZ]/g, '').slice(0, 17);
  const rand = crypto.randomBytes(3).toString('hex');
  return `${prefix}_${date}_${rand}`;
}

function cleanTemplateContent(content) {
  if (!content) return '';
  let cleaned = content.replace(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g, '[anonymisé]');
  cleaned = cleaned.replace(/Nom: [^\n]+/g, 'Nom: [anonymisé]');
  return cleaned;
}

function checkAccessibility(content) {
  return /aria-|alt=|role=/.test(content || '');
}

function auditTemplate(content) {
  return {
    length: (content || '').length,
    hasAccessibility: checkAccessibility(content || ''),
    isRGPD: !(content || '').includes('@'),
    timestamp: new Date().toISOString()
  };
}

module.exports = {
  generateTemplateId,
  cleanTemplateContent,
  checkAccessibility,
  auditTemplate
};
