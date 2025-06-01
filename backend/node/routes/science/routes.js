// Route pour la gestion scientifique (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { scienceController } = require('../../controllers/scienceController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), scienceController.list);
router.post('/', checkJwt, checkRole(['admin']), scienceController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), scienceController.get);
router.put('/:id', checkJwt, checkRole(['admin']), scienceController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), scienceController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), scienceController.graphql);

module.exports = router;
