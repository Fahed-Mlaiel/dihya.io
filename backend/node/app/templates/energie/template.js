// Template de routes énergie avancé (REST, GraphQL, sécurité, i18n, plugins, RGPD, SEO, multitenancy, audit, IA, tests)
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginLoader } = require('../../../../core/middleware');
const { getConsommation, createProduction, updateProduction, deleteProduction } = require('./controller');
const router = express.Router();

router.use(i18nMiddleware);
router.use(checkJwt);
router.use(auditLog);
router.use(pluginLoader);

/**
 * @route GET /energie/consommation
 * @desc Liste des consommations (multi-tenant, filtrage, pagination, i18n)
 * @access Roles: admin, opérateur, utilisateur, invité
 */
router.get('/consommation', checkRole(['admin', 'operator', 'user', 'guest']), getConsommation);

/**
 * @route POST /energie/production
 * @desc Déclaration de production (validation, audit, RGPD)
 * @access Roles: admin, opérateur
 */
router.post('/production', checkRole(['admin', 'operator']), createProduction);

/**
 * @route PUT /energie/production/:id
 * @desc Mise à jour d'une production
 * @access Roles: admin, opérateur
 */
router.put('/production/:id', checkRole(['admin', 'operator']), updateProduction);

/**
 * @route DELETE /energie/production/:id
 * @desc Suppression d'une production (audit, anonymisation RGPD)
 * @access Roles: admin
 */
router.delete('/production/:id', checkRole(['admin']), deleteProduction);

module.exports = router;
