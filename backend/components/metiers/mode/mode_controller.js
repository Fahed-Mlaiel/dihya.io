// Mode Controller – Dihya Coding
// Sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, documentation, logs, export, anonymisation
import ModeManager from './index.js';

export const ModeController = {
  async addCollection(req, res) {
    // Validation, audit, plugins, IA, RGPD
    const mode = new ModeManager({ lang: req.lang, role: req.user?.role });
    const result = await mode.addCollection(req.body);
    res.status(201).json(result);
  },
  async exportData(req, res) {
    // Audit, anonymisation, export
    const mode = new ModeManager({ lang: req.lang, role: req.user?.role });
    const data = await mode.exportData();
    res.json({ data });
  }
};
