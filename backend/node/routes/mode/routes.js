// Route pour la gestion des modes (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { modeController } = require('../../controllers/modeController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), modeController.list);
router.post('/', checkJwt, checkRole(['admin']), modeController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), modeController.get);
router.put('/:id', checkJwt, checkRole(['admin']), modeController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), modeController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), modeController.graphql);

module.exports = router;
