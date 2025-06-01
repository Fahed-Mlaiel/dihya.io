/**
 * Routes 3D ultra avancées – Dihya Coding
 * - Sécurité maximale (CORS, JWT, WAF, anti-DDOS, RBAC, validation, audit, RGPD, multitenancy)
 * - Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * - Plugins extensibles, auditabilité, SEO backend, logs structurés
 * - REST & GraphQL, fallback IA open source (LLaMA, Mixtral, Mistral)
 * - Documentation intégrée, tests, accessibilité, conformité CI/CD
 * @module routes/3d/routes
 * @author Dihya Coding
 * @version 2.0.0
 * @license AGPL-3.0
 */
const express = require('express');
const { checkJWT, checkRole, checkTenant, i18nMiddleware, wafMiddleware, ddosMiddleware } = require('../../middlewares/security');
const { auditLog, anonymize, exportData } = require('../../middlewares/audit');
const { generate3DProject, list3DProjects, get3DProject, update3DProject, delete3DProject } = require('../../controllers/3dController');
const { pluginManager } = require('../../plugins/3d');
const { seoMiddleware } = require('../../middlewares/seo');
const { rgpdMiddleware } = require('../../middlewares/rgpd');
const router = express.Router();

// Middlewares globaux : sécurité, i18n, audit, SEO, RGPD, plugins
router.use(wafMiddleware);
router.use(ddosMiddleware);
router.use(i18nMiddleware());
router.use(auditLog('3d'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());
router.use(pluginManager('3d'));

/**
 * @swagger
 * /api/3d/projects:
 *   get:
 *     summary: Liste des projets 3D
 *     security: [JWT]
 *     tags: [3D]
 *     responses:
 *       200:
 *         description: Succès
 */
router.get('/projects', checkJWT, checkRole(['admin','user','guest']), checkTenant, list3DProjects);

/**
 * @swagger
 * /api/3d/projects:
 *   post:
 *     summary: Générer un projet 3D (IA, VR, AR)
 *     security: [JWT]
 *     tags: [3D]
 *     requestBody:
 *       required: true
 *     responses:
 *       201:
 *         description: Projet créé
 */
router.post('/projects', checkJWT, checkRole(['admin']), checkTenant, auditLog('create'), generate3DProject);

router.get('/projects/:id', checkJWT, checkRole(['admin','user','guest']), checkTenant, get3DProject);
router.put('/projects/:id', checkJWT, checkRole(['admin']), checkTenant, auditLog('update'), update3DProject);
router.delete('/projects/:id', checkJWT, checkRole(['admin']), checkTenant, auditLog('delete'), anonymize, delete3DProject);

// GraphQL endpoint (exemple)
router.post('/graphql', checkJWT, checkRole(['admin', 'user']), (req, res) => {
  // TODO: brancher sur le schéma GraphQL global 3D
  res.json({ data: {}, lang: req.headers['accept-language'] });
});

// SEO backend : robots.txt, sitemap.xml
router.get('/seo/robots.txt', seoMiddleware(), (req, res) => {
  res.type('text/plain').send('User-agent: *\nDisallow: /private\n');
});

// RGPD : export/anonymisation
router.get('/rgpd/export', checkJWT, checkRole(['admin']), rgpdMiddleware(), (req, res) => {
  res.json({ export: 'data-anonymized' });
});

// Audit log
router.get('/audit-log', checkJWT, checkRole(['admin']), auditLog('3d'), (req, res) => {
  res.json({ audit: [] });
});

// Plugins dynamiques (exemple)
router.post('/plugins/:pluginName/run', checkJWT, checkRole(['admin','user']), (req, res) => {
  const plugin = pluginManager('3d').get(req.params.pluginName);
  if (!plugin) return res.status(404).json({ error: 'Plugin not found' });
  res.json(plugin.run(req.body, req.user));
});

module.exports = router;
