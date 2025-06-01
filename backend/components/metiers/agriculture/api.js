// api.js – REST/GraphQL API pour le module Agriculture (Dihya Coding)
const express = require('express');
const { validateJWT, rbac, audit, i18n, waf, ddos, seo, multitenancy, pluginLoader } = require('../../../core/middleware');
const AgricultureController = require('./agriculture_controller');
const router = express.Router();

router.use(waf(), ddos(), seo('agriculture'), multitenancy(), i18n(), audit());
router.use(validateJWT());

router.get('/', rbac(['admin', 'exploitant', 'user', 'invite']), async (req, res) => {
  const lang = req.lang || 'fr';
  audit.log({ event: 'agriculture_list', user: req.user });
  res.json({ message: req.t('agriculture_list'), lang });
});

router.post('/plugin', rbac(['admin']), pluginLoader('agriculture'), async (req, res) => {
  res.json({ success: true });
});

// ... autres routes avancées (CRUD, Export, Anonymisation, Fallback-AI, etc.) ...

module.exports = router;
