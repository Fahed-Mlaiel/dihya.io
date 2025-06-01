// Route pour la gestion du tourisme (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { tourismeController } = require('../../controllers/tourismeController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), tourismeController.list);
router.post('/', checkJwt, checkRole(['admin']), tourismeController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), tourismeController.get);
router.put('/:id', checkJwt, checkRole(['admin']), tourismeController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), tourismeController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), tourismeController.graphql);

module.exports = router;
