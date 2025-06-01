// Route pour la gestion du sport (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { sportController } = require('../../controllers/sportController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), sportController.list);
router.post('/', checkJwt, checkRole(['admin']), sportController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), sportController.get);
router.put('/:id', checkJwt, checkRole(['admin']), sportController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), sportController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), sportController.graphql);

module.exports = router;
