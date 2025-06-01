// Route pour la recherche avancée (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { rechercheController } = require('../../controllers/rechercheController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user', 'invite']), rechercheController.search);
router.post('/graphql', checkJwt, checkRole(['admin', 'user', 'invite']), rechercheController.graphql);

module.exports = router;
