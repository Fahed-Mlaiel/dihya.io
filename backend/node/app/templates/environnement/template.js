// Template de routes environnement avancé (REST, GraphQL, sécurité, i18n, plugins, RGPD, SEO, multitenancy, audit, IA, tests)
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginLoader } = require('../../../../core/middleware');
const { getIndicateurs, createMesure, updateMesure, deleteMesure } = require('./controller');
const router = express.Router();

router.use(i18nMiddleware);
router.use(checkJwt);
router.use(auditLog);
router.use(pluginLoader);

/**
 * @route GET /environnement/indicateurs
 * @desc Liste des indicateurs (multi-tenant, filtrage, pagination, i18n)
 * @access Roles: admin, analyst, user, guest
 */
router.get('/indicateurs', checkRole(['admin', 'analyst', 'user', 'guest']), getIndicateurs);

/**
 * @route POST /environnement/mesure
 * @desc Ajout d'une mesure (validation, audit, RGPD)
 * @access Roles: admin, analyst
 */
router.post('/mesure', checkRole(['admin', 'analyst']), createMesure);

/**
 * @route PUT /environnement/mesure/:id
 * @desc Mise à jour d'une mesure
 * @access Roles: admin, analyst
 */
router.put('/mesure/:id', checkRole(['admin', 'analyst']), updateMesure);

/**
 * @route DELETE /environnement/mesure/:id
 * @desc Suppression d'une mesure (audit, anonymisation RGPD)
 * @access Roles: admin
 */
router.delete('/mesure/:id', checkRole(['admin']), deleteMesure);

module.exports = router;
