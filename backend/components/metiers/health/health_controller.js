// Health Controller – Dihya Coding
// Sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, documentation, logs, export, anonymisation
import * as service from './services/healthService.js';

export const HealthController = {
  async getAppointments(req, res) {
    // Sécurité, i18n, audit, plugins, SEO
    const appointments = await service.getAppointments(req);
    res.json({ appointments, lang: req.lang });
  },
  async createAppointment(req, res) {
    // Validation, audit, plugins, IA, RGPD
    const appointment = await service.createAppointment(req.body, req.user);
    res.status(201).json({ appointment });
  },
  async updateAppointment(req, res) {
    // RBAC, audit, plugins
    const appointment = await service.updateAppointment(req.params.id, req.body, req.user);
    res.json({ appointment });
  },
  async deleteAppointment(req, res) {
    // Audit, anonymisation, export
    await service.deleteAppointment(req.params.id, req.user);
    res.status(204).end();
  }
};
