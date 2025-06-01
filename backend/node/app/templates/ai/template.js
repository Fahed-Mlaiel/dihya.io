/**
 * Template métier Intelligence Artificielle – Dihya Coding
 * @module iaTemplate
 * @description API RESTful & GraphQL, multitenant, sécurité, i18n, plugins, IA fallback, RGPD, SEO, tests, etc.
 * @author Dihya Coding
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, rateLimiter, wafMiddleware } = require('../../../../src/middleware');
const { runInference, listModels } = require('../../../../src/services/iaService');
const router = express.Router();

/**
 * @swagger
 * /api/ia/inference:
 *   post:
 *     summary: Exécuter un modèle IA (sécurisé, RGPD, plugins)
 *     tags: [IA]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               model:
 *                 type: string
 *               input:
 *                 type: object
 *     responses:
 *       200:
 *         description: Résultat de l’inférence
 */
router.post('/inference',
  checkJwt,
  checkRole(['admin', 'data scientist', 'user']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const { model, input } = req.body;
    // Validation RGPD, plugins, IA fallback
    const result = await runInference({ model, input, tenant: req.tenant });
    res.status(200).json({ result, i18n: req.i18n });
  }
);

/**
 * @swagger
 * /api/ia/models:
 *   get:
 *     summary: Liste des modèles IA (multilingue, sécurisé)
 *     tags: [IA]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Liste des modèles
 */
router.get('/models',
  checkJwt,
  checkRole(['admin', 'data scientist', 'user', 'invité']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const models = await listModels(req.tenant);
    res.json({ models, i18n: req.i18n });
  }
);

module.exports = router;
