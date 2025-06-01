// Route pour la gestion vocale (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { voiceController } = require('../../controllers/voiceController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), voiceController.list);
router.post('/', checkJwt, checkRole(['admin']), voiceController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), voiceController.get);
router.put('/:id', checkJwt, checkRole(['admin']), voiceController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), voiceController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), voiceController.graphql);

module.exports = router;
