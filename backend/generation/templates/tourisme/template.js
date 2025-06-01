// Template backend Tourisme pour Dihya Coding
// REST, multilingue, multi-tenant, sécurité avancée, plugins, audit, RGPD

const express = require('express');
const { validateTourismeInput, getCurrentTenant, getCurrentUser, logTourismeEvent } = require('../utils');
const { requireRole, jwtAuth } = require('../../../../security');
const { runTourismePlugins } = require('../../../../plugins');
const router = express.Router();

function getLocale(req, res, next) {
  req.locale = req.headers['x-locale'] || 'fr';
  next();
}

router.post('/create', jwtAuth, requireRole(['admin', 'user']), getLocale, (req, res) => {
  validateTourismeInput(req.body);
  const tenant = getCurrentTenant(req);
  const user = getCurrentUser(req);
  const result = runTourismePlugins(req.body, req.locale, tenant);
  logTourismeEvent(user, tenant, req.body, result);
  res.json({ status: 'success', tourisme: result });
});

module.exports = router;
