// Gamer Controller – Dihya Coding
// Sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, documentation, logs, export, anonymisation
import * as service from './services/gamerService.js';

export const GamerController = {
  async getTournaments(req, res) {
    // Sécurité, i18n, audit, plugins, SEO
    const tournaments = await service.getTournaments(req);
    res.json({ tournaments, lang: req.lang });
  },
  async createTournament(req, res) {
    // Validation, audit, plugins, IA, RGPD
    const tournament = await service.createTournament(req.body, req.user);
    res.status(201).json({ tournament });
  },
  async updateTournament(req, res) {
    // RBAC, audit, plugins
    const tournament = await service.updateTournament(req.params.id, req.body, req.user);
    res.json({ tournament });
  },
  async deleteTournament(req, res) {
    // Audit, anonymisation, export
    await service.deleteTournament(req.params.id, req.user);
    res.status(204).end();
  }
};
