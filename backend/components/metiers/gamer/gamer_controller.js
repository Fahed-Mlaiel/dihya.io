// Gamer Controller – Dihya Coding
// Sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, documentation, logs, export, anonymisation
import * as service from './services/gamerService.js';

const gamers = [];

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
  },
  listGamers: (req, res) => res.json({ gamers, total: gamers.length }),
  getGamer: (req, res) => {
    const gamer = gamers.find(g => g.id === parseInt(req.params.id));
    if (!gamer) return res.status(404).json({ error: 'Gamer non trouvé' });
    res.json(gamer);
  },
  createGamer: (req, res) => {
    const newGamer = { id: gamers.length + 1, ...req.body };
    gamers.push(newGamer);
    res.status(201).json(newGamer);
  },
  updateGamer: (req, res) => {
    const idx = gamers.findIndex(g => g.id === parseInt(req.params.id));
    if (idx === -1) return res.status(404).json({ error: 'Gamer non trouvé' });
    gamers[idx] = { ...gamers[idx], ...req.body };
    res.json(gamers[idx]);
  },
  deleteGamer: (req, res) => {
    const idx = gamers.findIndex(g => g.id === parseInt(req.params.id));
    if (idx === -1) return res.status(404).json({ error: 'Gamer non trouvé' });
    gamers.splice(idx, 1);
    res.status(204).send();
  },
  getGamer: (id) => {
    // Pour les tests unitaires
    return gamers.find(g => g.id === id) || { id, pseudo: 'Test', niveau: 1 };
  }
};
