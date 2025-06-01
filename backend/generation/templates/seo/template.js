// SEO Template backend pour Dihya Coding
// REST, multilingue, multi-tenant, sécurité avancée, plugins, logs structurés, RGPD

const express = require('express');
const { validateSEOInput, getCurrentTenant, getCurrentUser, logSEOEvent } = require('../utils');
const { requireRole, jwtAuth } = require('../../../../security');
const { runSEOPlugins } = require('../../../../plugins');
const router = express.Router();

// Middleware internationalisation (exemple simplifié)
function getLocale(req, res, next) {
  req.locale = req.headers['x-locale'] || 'fr';
  next();
}

router.post('/optimize', jwtAuth, requireRole(['admin', 'user']), getLocale, (req, res) => {
  // Validation stricte (anti-XSS, anti-injection, RGPD)
  validateSEOInput(req.body);
  const tenant = getCurrentTenant(req);
  const user = getCurrentUser(req);
  const result = runSEOPlugins(req.body, req.locale, tenant);
  logSEOEvent(user, tenant, req.body, result);
  res.json({ status: 'success', seo: result });
});

router.get('/robots.txt', getLocale, (req, res) => {
  const tenant = getCurrentTenant(req);
  res.type('text/plain').send(`User-agent: *\nDisallow: /private/\nSitemap: /seo/sitemap.xml?locale=${req.locale}&tenant=${tenant}`);
});

router.get('/sitemap.xml', getLocale, (req, res) => {
  const tenant = getCurrentTenant(req);
  res.type('application/xml').send(`<?xml version='1.0' encoding='UTF-8'?>\n<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n  <url><loc>https://${tenant}.dihya.com/${req.locale}/</loc></url>\n</urlset>`);
});

module.exports = router;
