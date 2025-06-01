/**
 * Routes Arts - Gestion avancée de projets artistiques (expos, IA, audit, etc.)
 * Sécurité maximale, multilingue, multitenancy, plugins, audit, RGPD
 * @module routes/arts/routes
 * @see GraphQL support inclus
 */
const express = require('express');
const { checkJWT, checkRole, checkTenant, i18nMiddleware, wafMiddleware, ddosMiddleware } = require('../../middlewares/security');
const { auditLog, anonymize, exportData } = require('../../middlewares/audit');
const { createArtProject, listArtProjects, getArtProject, updateArtProject, deleteArtProject } = require('../../controllers/artsController');
const router = express.Router();

router.get('/', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, listArtProjects);
router.post('/', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, createArtProject);
router.get('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, getArtProject);
router.put('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, updateArtProject);
router.delete('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, anonymize, deleteArtProject);

// GraphQL endpoint (exemple)
// router.use('/graphql', require('../../graphql/arts'));

module.exports = router;
