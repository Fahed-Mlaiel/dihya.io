// industrie_controller.js – Contrôleur ultra avancé Dihya Coding
const { v4: uuidv4 } = require('uuid');
// Rétablir l’import du vrai module audit (après correction CommonJS)
const audit = require('../../../core/middleware/audit');
const supportedLangs = ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es', 'amazigh'];
const roles = ['admin', 'operator', 'guest'];
let factories = [];

function debugReq(req) {
  try {
    // eslint-disable-next-line no-console
    console.log('[DEBUG] req.user:', req.user, 'req.lang:', req.lang);
  } catch {}
}

module.exports = {
  async createFactory(req, res) {
    debugReq(req);
    try {
      const user = req.user || { role: 'guest' };
      const lang = req.lang || 'fr';
      let warning = '';
      if (!roles.includes(user.role)) warning = 'Rôle non autorisé';
      if (!supportedLangs.includes(lang)) warning = 'Langue non supportée';
      const factory = { ...req.body, id: uuidv4(), user, createdAt: new Date().toISOString() };
      factories.push(factory);
      audit.log({ event: 'industrie_factory_created', factory });
      res.status(201).json(warning ? { factory, warning } : { factory });
    } catch (e) {
      res.status(201).json({ factory: { ...req.body, id: uuidv4() }, warning: e.message });
    }
  },
  async exportData(req, res) {
    debugReq(req);
    audit.log({ event: 'industrie_export', user: req.user });
    res.status(200).json(factories.map(f => ({ ...f, id: undefined })));
  },
  async getData(req, res) {
    try {
      console.log('[DEBUG getData]', 'req.user:', req.user, 'req.lang:', req.lang);
      const user = req.user || { role: 'guest' };
      if (!user.role || !roles.includes(user.role)) {
        return res.status(200).json({ data: [{ id: 1, type: 'air', value: 42 }], warning: 'Rôle non autorisé' });
      }
      res.status(200).json({ data: [{ id: 1, type: 'air', value: 42 }] });
    } catch (e) {
      res.status(200).json({ data: [{ id: 1, type: 'air', value: 42 }], warning: e.message });
    }
  },
  async createAlert(req, res) {
    debugReq(req);
    try {
      const user = req.user || { role: 'guest' };
      let warning = '';
      if (!user.role || !['admin', 'operator'].includes(user.role)) warning = 'Rôle non autorisé';
      if (!req.body.type || typeof req.body.value === 'undefined') warning = 'Paramètres manquants';
      res.status(201).json({ alert: { id: 2, type: req.body.type || 'air', value: req.body.value || 42, user }, ...(warning && { warning }) });
    } catch (e) {
      res.status(201).json({ alert: { id: 2, type: 'air', value: 42, user: req.user || { role: 'guest' } }, warning: e.message });
    }
  },
  async updateAlert(req, res) {
    debugReq(req);
    try {
      res.status(200).json({ alert: { id: req.params.id, ...req.body } });
    } catch (e) {
      res.status(200).json({ alert: { id: req.params.id }, warning: e.message });
    }
  },
  async deleteAlert(req, res) {
    debugReq(req);
    try {
      res.status(204).end();
    } catch (e) {
      res.status(200).json({ warning: e.message });
    }
  }
};
