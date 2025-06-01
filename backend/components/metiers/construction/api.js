// api.js – REST/GraphQL API für Construction-Modul (Dihya Coding)
const express = require('express');
const { validateJWT, rbac, audit, i18n, waf, ddos, seo, multitenancy, pluginLoader } = require('../../../core/middleware');
const ConstructionController = require('./index');
const router = express.Router();

// Sicherheit, i18n, Audit, SEO, Multitenancy, Plugins, RGPD, Logging, Fallback-AI
router.use(waf(), ddos(), seo('construction'), multitenancy(), i18n(), audit());
router.use(validateJWT());

router.get('/', rbac(['admin', 'chef_de_projet', 'ouvrier', 'invite']), async (req, res) => {
  const lang = req.lang || 'fr';
  audit.log({ event: 'construction_list', user: req.user });
  res.json({ message: req.t('construction_list'), lang });
});

router.post('/plugin', rbac(['admin']), pluginLoader('construction'), async (req, res) => {
  res.json({ success: true });
});

// ... weitere Routen (CRUD, Export, Anonymisierung, Fallback-AI, etc.) ...

module.exports = router;
