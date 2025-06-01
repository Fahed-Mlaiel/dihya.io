// Route pour la gestion sociale (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { socialController } = require('../../controllers/socialController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), socialController.list);
router.post('/', checkJwt, checkRole(['admin']), socialController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), socialController.get);
router.put('/:id', checkJwt, checkRole(['admin']), socialController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), socialController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), socialController.graphql);

module.exports = router;
