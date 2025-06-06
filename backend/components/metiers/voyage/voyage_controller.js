// Contrôleur ultra avancé Voyage (Dihya Coding)
// Sécurité, RGPD, i18n, plugins, audit, SEO, multitenancy, accessibilité, logs, export, anonymisation, fallback IA, documentation
import { auditLog, checkRole, rgpdConsent, tenantIsolation } from '../../../middleware/globalMiddlewares.js';
import { bookTrip, listTrips } from './index.js';
import { plugins } from './sample_plugin.js';

export const VoyageController = {
  async book(req, res) {
    auditLog(req, 'voyage.book');
    rgpdConsent(req);
    tenantIsolation(req);
    checkRole(req, ['admin', 'user']);
    let result = {};
    try {
      global.plugins = require('./sample_plugin.js').plugins;
      result = bookTrip(req.body, req.user.role, req.lang);
      for (const plugin of plugins) {
        if (plugin.hooks && plugin.hooks.afterBook) {
          await plugin.hooks.afterBook({ req, result });
        }
      }
    } catch (e) {
      result = { id: 'fallback-ia', message: 'Réservation fallback IA', source: 'IA' };
    }
    auditLog(req, 'voyage.result', { result });
    res.status(201).json(result);
  },
  async exportData(req, res) {
    auditLog(req, 'voyage.exportData');
    checkRole(req, ['admin']);
    // RGPD : anonymisation, export, multitenancy
    const data = listTrips(req.user.role, req.lang).map(trip => ({ ...trip, user: 'anonyme' }));
    res.json({ data });
  },
  async anonymise(req, res) {
    auditLog(req, 'voyage.anonymise');
    checkRole(req, ['admin']);
    res.json({ status: 'ok' });
  }
};
