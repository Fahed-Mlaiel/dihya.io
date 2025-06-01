// Route pour la gestion du transport (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { transportController } = require('../../controllers/transportController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), transportController.list);
router.post('/', checkJwt, checkRole(['admin']), transportController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), transportController.get);
router.put('/:id', checkJwt, checkRole(['admin']), transportController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), transportController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), transportController.graphql);

module.exports = router;
