// Route pour la gestion des previews (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { previewController } = require('../../controllers/previewController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), previewController.list);
router.post('/', checkJwt, checkRole(['admin']), previewController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), previewController.get);
router.put('/:id', checkJwt, checkRole(['admin']), previewController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), previewController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), previewController.graphql);

module.exports = router;
