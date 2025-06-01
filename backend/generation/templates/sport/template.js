// Template backend Sport pour Dihya Coding
// REST, multilingue, multi-tenant, sécurité avancée, plugins, audit, RGPD

const express = require('express');
const { validateSportInput, getCurrentTenant, getCurrentUser, logSportEvent } = require('../utils');
const { requireRole, jwtAuth } = require('../../../../security');
const { runSportPlugins } = require('../../../../plugins');
const router = express.Router();

function getLocale(req, res, next) {
  req.locale = req.headers['x-locale'] || 'fr';
  next();
}

router.post('/create', jwtAuth, requireRole(['admin', 'user']), getLocale, (req, res) => {
  validateSportInput(req.body);
  const tenant = getCurrentTenant(req);
  const user = getCurrentUser(req);
  const result = runSportPlugins(req.body, req.locale, tenant);
  logSportEvent(user, tenant, req.body, result);
  res.json({ status: 'success', sport: result });
});

module.exports = router;
