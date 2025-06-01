// Route pour la gestion de la restauration (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { restaurationController } = require('../../controllers/restaurationController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), restaurationController.list);
router.post('/', checkJwt, checkRole(['admin']), restaurationController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), restaurationController.get);
router.put('/:id', checkJwt, checkRole(['admin']), restaurationController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), restaurationController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), restaurationController.graphql);

module.exports = router;
