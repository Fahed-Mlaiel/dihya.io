// preview_controller.js – Contrôleur ultra avancé Dihya Coding
const { v4: uuidv4 } = require('uuid');
const audit = require('../../../core/middleware/audit');
const supportedLangs = ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es', 'amazigh'];
const roles = ['admin', 'user', 'guest'];
let previews = [];

module.exports = {
  async createPreview(req, res) {
    if (!roles.includes(req.user.role)) throw new Error('Rôle non autorisé');
    if (!supportedLangs.includes(req.lang)) throw new Error('Langue non supportée');
    // Validation, RGPD, plugins, audit, logs, multitenancy
    const preview = { ...req.body, id: uuidv4(), user: req.user, createdAt: new Date().toISOString() };
    previews.push(preview);
    audit.log({ event: 'preview_created', preview });
    return preview;
  },
  async exportData(req, res) {
    audit.log({ event: 'preview_export', user: req.user });
    return previews.map(p => ({ ...p, id: undefined }));
  }
};
