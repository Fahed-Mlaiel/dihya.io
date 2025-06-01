// Route pour la gestion de la santé (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { santeController } = require('../../controllers/santeController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), santeController.list);
router.post('/', checkJwt, checkRole(['admin']), santeController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), santeController.get);
router.put('/:id', checkJwt, checkRole(['admin']), santeController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), santeController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), santeController.graphql);

module.exports = router;
