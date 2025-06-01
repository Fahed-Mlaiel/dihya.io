// Route pour la validation avancée (REST, sécurité, i18n, audit, plugins, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { validatorsController } = require('../../controllers/validatorsController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.post('/input', checkJwt, checkRole(['admin', 'user']), validatorsController.validateInput);
router.post('/export', checkJwt, checkRole(['admin']), validatorsController.exportValidation);

module.exports = router;
