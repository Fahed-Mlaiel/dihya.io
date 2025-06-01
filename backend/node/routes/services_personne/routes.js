// Route pour la gestion des services à la personne (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { servicesPersonneController } = require('../../controllers/servicesPersonneController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), servicesPersonneController.list);
router.post('/', checkJwt, checkRole(['admin']), servicesPersonneController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), servicesPersonneController.get);
router.put('/:id', checkJwt, checkRole(['admin']), servicesPersonneController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), servicesPersonneController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), servicesPersonneController.graphql);

module.exports = router;
