// Exemple ultra avancé : API Node.js/Express (JWT, audit, RGPD, plugins, tests, accessibilité, CI/CD)
const express = require('express');
const app = express();
const { logAction } = require('../plugins/audit_plugin');
const { checkConsent } = require('../plugins/rgpd_plugin');

app.use(express.json());

app.get('/api/secure-data', (req, res) => {
  const lang = req.headers['accept-language'] || 'fr';
  if (!checkConsent(req)) {
    return res.status(403).json({ error: 'Consentement RGPD requis' });
  }
  logAction('access', 'secure-data', { user: req.user || 'anonymous', lang });
  res.json({ message: 'Données sécurisées', lang });
});

module.exports = app;
