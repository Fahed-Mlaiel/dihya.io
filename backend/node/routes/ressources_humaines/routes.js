// Route pour la gestion des ressources humaines (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { rhController } = require('../../controllers/rhController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), rhController.list);
router.post('/', checkJwt, checkRole(['admin']), rhController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), rhController.get);
router.put('/:id', checkJwt, checkRole(['admin']), rhController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), rhController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), rhController.graphql);

module.exports = router;
