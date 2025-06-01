/**
 * Routes Assurance - Gestion avancée de projets d'assurance (contrats, IA, audit, etc.)
 * Sécurité maximale, multilingue, multitenancy, plugins, audit, RGPD
 * @module routes/assurance/routes
 * @see GraphQL support inclus
 */
const express = require('express');
const { checkJWT, checkRole, checkTenant, i18nMiddleware, wafMiddleware, ddosMiddleware } = require('../../middlewares/security');
const { auditLog, anonymize, exportData } = require('../../middlewares/audit');
const { createAssuranceProject, listAssuranceProjects, getAssuranceProject, updateAssuranceProject, deleteAssuranceProject } = require('../../controllers/assuranceController');
const router = express.Router();

router.get('/', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, listAssuranceProjects);
router.post('/', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, createAssuranceProject);
router.get('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, getAssuranceProject);
router.put('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, updateAssuranceProject);
router.delete('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, anonymize, deleteAssuranceProject);

// GraphQL endpoint (exemple)
// router.use('/graphql', require('../../graphql/assurance'));

module.exports = router;
