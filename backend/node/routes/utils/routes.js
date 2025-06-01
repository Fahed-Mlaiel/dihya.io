// Route utilitaire (REST, sécurité, i18n, audit, plugins, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { utilsController } = require('../../controllers/utilsController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/status', utilsController.status);
router.get('/health', utilsController.health);
router.get('/info', utilsController.info);

module.exports = router;
