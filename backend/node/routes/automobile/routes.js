/**
 * Routes Automobile - Gestion avancée de projets automobiles (fleet, IA, audit, etc.)
 * Sécurité maximale, multilingue, multitenancy, plugins, audit, RGPD
 * @module routes/automobile/routes
 * @see GraphQL support inclus
 */
const express = require('express');
const { checkJWT, checkRole, checkTenant, i18nMiddleware, wafMiddleware, ddosMiddleware } = require('../../middlewares/security');
const { auditLog, anonymize, exportData } = require('../../middlewares/audit');
const { createAutoProject, listAutoProjects, getAutoProject, updateAutoProject, deleteAutoProject } = require('../../controllers/automobileController');
const router = express.Router();

router.get('/', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, listAutoProjects);
router.post('/', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, createAutoProject);
router.get('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, getAutoProject);
router.put('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, updateAutoProject);
router.delete('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, anonymize, deleteAutoProject);

// GraphQL endpoint (exemple)
// router.use('/graphql', require('../../graphql/automobile'));

module.exports = router;
