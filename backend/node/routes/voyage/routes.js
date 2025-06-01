// Route pour la gestion des voyages (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { voyageController } = require('../../controllers/voyageController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), voyageController.list);
router.post('/', checkJwt, checkRole(['admin']), voyageController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), voyageController.get);
router.put('/:id', checkJwt, checkRole(['admin']), voyageController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), voyageController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), voyageController.graphql);

module.exports = router;
