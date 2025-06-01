// api.js – REST/GraphQL API für 3D-Modul (Dihya Coding)
const express = require('express');
const { validateJWT, rbac, audit, i18n, waf, ddos, seo, multitenancy, pluginLoader } = require('../../../core/middleware');
const ThreeController = require('./three_controller');
const router = express.Router();

// Sicherheit, i18n, Audit, SEO, Multitenancy, Plugins, RGPD, Logging, Fallback-AI
router.use(waf(), ddos(), seo('3d'), multitenancy(), i18n(), audit());
router.use(validateJWT());

router.get('/', rbac(['admin', 'user']), async (req, res) => {
  const lang = req.lang || 'fr';
  audit.log({ event: '3d_list', user: req.user });
  res.json({ message: req.t('3d_list'), lang });
});

router.post('/plugin', rbac(['admin']), pluginLoader('3d'), async (req, res) => {
  res.json({ success: true });
});

// ... weitere Routen (CRUD, Export, Anonymisierung, Fallback-AI, etc.) ...

module.exports = router;
