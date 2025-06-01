/**
 * Routes Administration Publique - Gestion avancée (démarches, open data, audit, etc.)
 * Sécurité maximale, multilingue, multitenancy, plugins, audit, RGPD
 * @module routes/administration_publique/routes
 * @see GraphQL support inclus
 */
const express = require('express');
const { checkJWT, checkRole, checkTenant, i18nMiddleware, wafMiddleware, ddosMiddleware } = require('../../middlewares/security');
const { auditLog, anonymize, exportData } = require('../../middlewares/audit');
const { createAdminProject, listAdminProjects, getAdminProject, updateAdminProject, deleteAdminProject } = require('../../controllers/administrationPubliqueController');
const router = express.Router();

router.get('/', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, listAdminProjects);
router.post('/', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, createAdminProject);
router.get('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, getAdminProject);
router.put('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, updateAdminProject);
router.delete('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, anonymize, deleteAdminProject);

// GraphQL endpoint (exemple)
// router.use('/graphql', require('../../graphql/administration_publique'));

module.exports = router;
