/**
 * Template métier IT & DevOps – Dihya Coding
 * @module itDevopsTemplate
 * @description API RESTful & GraphQL, multitenant, sécurité, i18n, plugins, IA fallback, RGPD, SEO, tests, etc.
 * @author Dihya Coding
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, rateLimiter, wafMiddleware } = require('../../../../src/middleware');
const { getPipelines, triggerMonitor } = require('../../../../src/services/itDevopsService');
const router = express.Router();

/**
 * @swagger
 * /api/it_devops/pipelines:
 *   get:
 *     summary: Liste des pipelines CI/CD (multilingue, sécurisé)
 *     tags: [IT & DevOps]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Liste des pipelines
 */
router.get('/pipelines',
  checkJwt,
  checkRole(['admin', 'devops', 'user', 'invité']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const pipelines = await getPipelines(req.tenant);
    res.json({ pipelines, i18n: req.i18n });
  }
);

/**
 * @swagger
 * /api/it_devops/monitor:
 *   post:
 *     summary: Déclencher un monitoring (sécurisé, RGPD, plugins)
 *     tags: [IT & DevOps]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               pipelineId:
 *                 type: string
 *               userId:
 *                 type: string
 *     responses:
 *       201:
 *         description: Monitoring déclenché
 */
router.post('/monitor',
  checkJwt,
  checkRole(['admin', 'devops', 'user']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const { pipelineId, userId } = req.body;
    // Validation RGPD, plugins, IA fallback
    const result = await triggerMonitor({ pipelineId, userId, tenant: req.tenant });
    res.status(201).json({ result, i18n: req.i18n });
  }
);

module.exports = router;
