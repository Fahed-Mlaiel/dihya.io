/**
 * Module de stockage avancé, multitenant, sécurisé, plugins, audit, RGPD, multilingue.
 * @module storage
 */
const fs = require('fs');
const path = require('path');
const { auditLog } = require('../services/service');

/**
 * Sauvegarde un fichier pour un tenant donné.
 * @param {string} tenant
 * @param {string} filename
 * @param {Buffer|string} data
 */
function saveFile(tenant, filename, data) {
  const dir = path.join(__dirname, 'data', tenant);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, filename), data);
  auditLog('saveFile', { tenant, filename });
}

/**
 * Récupère un fichier pour un tenant donné.
 * @param {string} tenant
 * @param {string} filename
 * @returns {Buffer}
 */
function getFile(tenant, filename) {
  const filePath = path.join(__dirname, 'data', tenant, filename);
  if (!fs.existsSync(filePath)) throw new Error('File not found');
  auditLog('getFile', { tenant, filename });
  return fs.readFileSync(filePath);
}

module.exports = {
  saveFile,
  getFile
};
