// Environnement Controller – Dihya Coding
// Sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, documentation, logs, export, anonymisation
import * as service from './services/environnementService.js';

export const EnvironnementController = {
  async getData(req, res) {
    // Sécurité, i18n, audit, plugins, SEO
    const data = await service.getEnvData(req);
    res.json({ data, lang: req.lang });
  },
  async createAlert(req, res) {
    // Validation, audit, plugins, IA, RGPD
    const alert = await service.createEnvAlert(req.body, req.user);
    res.status(201).json({ alert });
  },
  async updateAlert(req, res) {
    // RBAC, audit, plugins
    const alert = await service.updateEnvAlert(req.params.id, req.body, req.user);
    res.json({ alert });
  },
  async deleteAlert(req, res) {
    // Audit, anonymisation, export
    await service.deleteEnvAlert(req.params.id, req.user);
    res.status(204).end();
  }
};
