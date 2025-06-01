// Route pour la gestion VR/AR (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { vrArController } = require('../../controllers/vrArController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), vrArController.list);
router.post('/', checkJwt, checkRole(['admin']), vrArController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), vrArController.get);
router.put('/:id', checkJwt, checkRole(['admin']), vrArController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), vrArController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), vrArController.graphql);

module.exports = router;
