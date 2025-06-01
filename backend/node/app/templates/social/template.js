/**
 * Template de routes RESTful et GraphQL pour la gestion de projets sociaux (IA, VR, AR, etc.)
 * Sécurité maximale (CORS, JWT, audit, WAF, anti-DDOS)
 * Internationalisation dynamique (fr, en, ar, ...)
 * Multitenancy, gestion des rôles, plugins, RGPD, SEO, fallback IA open source
 * @module social/template
 */

const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, wafMiddleware, ddosMiddleware, auditLogger } = require('../../utils/utils');
const { validateSocialProject } = require('../../validators/template');
const { getLlamaFallback } = require('../../utils/llama');
const router = express.Router();

/**
 * @swagger
 * /api/social/projects:
 *   get:
 *     summary: Liste des projets sociaux
 *     security: [BearerAuth]
 *     tags: [Social]
 *     responses:
 *       200:
 *         description: Succès
 */
router.get('/projects',
  wafMiddleware,
  ddosMiddleware,
  checkJwt,
  checkRole(['admin', 'user', 'invite']),
  i18nMiddleware,
  auditLogger,
  async (req, res) => {
    // TODO: fetch from DB
    res.json({ projects: [], i18n: req.i18n });
  }
);

/**
 * Création d'un projet social
 */
router.post('/projects',
  wafMiddleware,
  ddosMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLogger,
  validateSocialProject,
  async (req, res) => {
    // TODO: save to DB
    res.status(201).json({ message: req.i18n('project_created'), project: req.body });
  }
);

/**
 * Fallback IA open source (LLaMA, Mixtral, Mistral)
 */
router.post('/projects/ai-fallback',
  wafMiddleware,
  ddosMiddleware,
  checkJwt,
  checkRole(['admin']),
  i18nMiddleware,
  auditLogger,
  async (req, res) => {
    const result = await getLlamaFallback(req.body.prompt);
    res.json({ result });
  }
);

module.exports = router;
