// Template backend Transport pour Dihya Coding
// REST, multilingue, multi-tenant, sécurité avancée, plugins, audit, RGPD

const express = require('express');
const { validateTransportInput, getCurrentTenant, getCurrentUser, logTransportEvent } = require('../utils');
const { requireRole, jwtAuth } = require('../../../../security');
const { runTransportPlugins } = require('../../../../plugins');
const router = express.Router();

function getLocale(req, res, next) {
  req.locale = req.headers['x-locale'] || 'fr';
  next();
}

router.post('/create', jwtAuth, requireRole(['admin', 'user']), getLocale, (req, res) => {
  validateTransportInput(req.body);
  const tenant = getCurrentTenant(req);
  const user = getCurrentUser(req);
  const result = runTransportPlugins(req.body, req.locale, tenant);
  logTransportEvent(user, tenant, req.body, result);
  res.json({ status: 'success', transport: result });
});

module.exports = router;
