/**
 * Routes Agriculture - Gestion avancée de projets agricoles (IA, IoT, audit, etc.)
 * Sécurité maximale, multilingue, multitenancy, plugins, audit, RGPD
 * @module routes/agriculture/routes
 * @see GraphQL support inclus
 */
const express = require('express');
const { checkJWT, checkRole, checkTenant, i18nMiddleware, wafMiddleware, ddosMiddleware } = require('../../middlewares/security');
const { auditLog, anonymize, exportData } = require('../../middlewares/audit');
const { createAgriProject, listAgriProjects, getAgriProject, updateAgriProject, deleteAgriProject } = require('../../controllers/agricultureController');
const router = express.Router();

router.get('/', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, listAgriProjects);
router.post('/', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, createAgriProject);
router.get('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, getAgriProject);
router.put('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, updateAgriProject);
router.delete('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, anonymize, deleteAgriProject);

// GraphQL endpoint (exemple)
// router.use('/graphql', require('../../graphql/agriculture'));

module.exports = router;
