// Template backend Services à la Personne pour Dihya Coding
// REST, multilingue, multi-tenant, sécurité avancée, plugins, audit, RGPD

const express = require('express');
const { validateServiceInput, getCurrentTenant, getCurrentUser, logServiceEvent } = require('../utils');
const { requireRole, jwtAuth } = require('../../../../security');
const { runServicePlugins } = require('../../../../plugins');
const router = express.Router();

function getLocale(req, res, next) {
  req.locale = req.headers['x-locale'] || 'fr';
  next();
}

router.post('/create', jwtAuth, requireRole(['admin', 'user']), getLocale, (req, res) => {
  validateServiceInput(req.body);
  const tenant = getCurrentTenant(req);
  const user = getCurrentUser(req);
  const result = runServicePlugins(req.body, req.locale, tenant);
  logServiceEvent(user, tenant, req.body, result);
  res.json({ status: 'success', service: result });
});

module.exports = router;
