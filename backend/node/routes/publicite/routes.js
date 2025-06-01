// Route pour la gestion des publicités (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy, doc intégrée)
// Langues: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Rôles: admin, user, invité
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginMiddleware, tenantMiddleware } = require('../../middlewares');
const { publiciteController } = require('../../controllers/publiciteController');
const router = express.Router();

router.use(i18nMiddleware);
router.use(auditLog);
router.use(pluginMiddleware);
router.use(tenantMiddleware);

router.get('/', checkJwt, checkRole(['admin', 'user']), publiciteController.list);
router.post('/', checkJwt, checkRole(['admin']), publiciteController.create);
router.get('/:id', checkJwt, checkRole(['admin', 'user']), publiciteController.get);
router.put('/:id', checkJwt, checkRole(['admin']), publiciteController.update);
router.delete('/:id', checkJwt, checkRole(['admin']), publiciteController.remove);

router.post('/graphql', checkJwt, checkRole(['admin', 'user']), publiciteController.graphql);

module.exports = router;
