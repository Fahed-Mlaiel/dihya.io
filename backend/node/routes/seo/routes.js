// Route SEO backend (robots, sitemap dynamique, logs structurés, sécurité, i18n, audit, plugins, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { seoController } = require('../../controllers/seoController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/robots.txt', seoController.robots);
router.get('/sitemap.xml', seoController.sitemap);
router.get('/logs', checkJwt, checkRole(['admin']), seoController.logs);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), seoController.graphql);

module.exports = router;
