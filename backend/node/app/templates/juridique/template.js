/**
 * Template métier Juridique – Dihya Coding
 * @module juridiqueTemplate
 * @description API RESTful & GraphQL, multitenant, sécurité, i18n, plugins, IA fallback, RGPD, SEO, tests, etc.
 * @author Dihya Coding
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, rateLimiter, wafMiddleware } = require('../../../../src/middleware');
const { getCases, createContract } = require('../../../../src/services/juridiqueService');
const router = express.Router();

/**
 * @swagger
 * /api/juridique/cases:
 *   get:
 *     summary: Liste des dossiers juridiques (multilingue, sécurisé)
 *     tags: [Juridique]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Liste des dossiers
 */
router.get('/cases',
  checkJwt,
  checkRole(['admin', 'avocat', 'client', 'invité']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const cases = await getCases(req.tenant);
    res.json({ cases, i18n: req.i18n });
  }
);

/**
 * @swagger
 * /api/juridique/contract:
 *   post:
 *     summary: Créer un contrat (sécurisé, RGPD, plugins)
 *     tags: [Juridique]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               title:
 *                 type: string
 *               parties:
 *                 type: array
 *                 items:
 *                   type: string
 *               content:
 *                 type: string
 *     responses:
 *       201:
 *         description: Contrat créé
 */
router.post('/contract',
  checkJwt,
  checkRole(['admin', 'avocat']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const { title, parties, content } = req.body;
    // Validation RGPD, plugins, IA fallback
    const result = await createContract({ title, parties, content, tenant: req.tenant });
    res.status(201).json({ result, i18n: req.i18n });
  }
);

module.exports = router;
