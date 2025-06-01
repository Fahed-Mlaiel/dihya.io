/**
 * Template métier Journalisme – Dihya Coding
 * @module journalismeTemplate
 * @description API RESTful & GraphQL, multitenant, sécurité, i18n, plugins, IA fallback, RGPD, SEO, tests, etc.
 * @author Dihya Coding
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, rateLimiter, wafMiddleware } = require('../../../../src/middleware');
const { getArticles, publishArticle } = require('../../../../src/services/journalismeService');
const router = express.Router();

/**
 * @swagger
 * /api/journalisme/articles:
 *   get:
 *     summary: Liste des articles (multilingue, sécurisé)
 *     tags: [Journalisme]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Liste des articles
 */
router.get('/articles',
  checkJwt,
  checkRole(['admin', 'rédacteur', 'lecteur', 'invité']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const articles = await getArticles(req.tenant);
    res.json({ articles, i18n: req.i18n });
  }
);

/**
 * @swagger
 * /api/journalisme/publish:
 *   post:
 *     summary: Publier un article (sécurisé, RGPD, plugins)
 *     tags: [Journalisme]
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
 *               content:
 *                 type: string
 *               authorId:
 *                 type: string
 *     responses:
 *       201:
 *         description: Article publié
 */
router.post('/publish',
  checkJwt,
  checkRole(['admin', 'rédacteur']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const { title, content, authorId } = req.body;
    // Validation RGPD, plugins, IA fallback
    const result = await publishArticle({ title, content, authorId, tenant: req.tenant });
    res.status(201).json({ result, i18n: req.i18n });
  }
);

module.exports = router;
