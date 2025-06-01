// Route pour la gestion mobile (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { mobileController } = require('../../controllers/mobileController');
const router = express.Router();

// RESTful routes
router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), mobileController.list);
router.post('/', checkJwt, checkRole(['admin']), mobileController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), mobileController.get);
router.put('/:id', checkJwt, checkRole(['admin']), mobileController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), mobileController.remove);

// GraphQL endpoint (exemple)
router.post('/graphql', checkJwt, checkRole(['admin', 'user']), mobileController.graphql);

module.exports = router;
