// core_utils.js – Utilitaires ultra avancés, clé en main, pour tests métiers 3D
// Respecte la modularité, la conformité RGPD, l’audit, la sécurité et la performance

const { v4: uuidv4 } = require('uuid');

function generateId(prefix = 'obj') {
  return `${prefix}-${uuidv4()}`;
}

function deepClone(obj) {
  return JSON.parse(JSON.stringify(obj));
}

function isValidEmail(email) {
  return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email);
}

function auditLog(action, user, meta = {}) {
  return {
    id: generateId('audit'),
    action,
    user,
    meta,
    timestamp: new Date().toISOString()
  };
}

module.exports = {
  generateId,
  deepClone,
  isValidEmail,
  auditLog
};
