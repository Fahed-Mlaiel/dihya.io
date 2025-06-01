/**
 * Template de routes RESTful et GraphQL pour la gestion de projets touristiques
 * Sécurité maximale, i18n, multitenancy, plugins, RGPD, SEO, fallback IA
 * @module tourisme/template
 */

const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, wafMiddleware, ddosMiddleware, auditLogger } = require('../../utils/utils');
const { validateTourismeProject } = require('../../validators/template');
const { getLlamaFallback } = require('../../utils/llama');
const router = express.Router();

router.get('/projects',
  wafMiddleware,
  ddosMiddleware,
  checkJwt,
  checkRole(['admin', 'user', 'invite']),
  i18nMiddleware,
  auditLogger,
  async (req, res) => {
    res.json({ projects: [], i18n: req.i18n });
  }
);

router.post('/projects',
  wafMiddleware,
  ddosMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLogger,
  validateTourismeProject,
  async (req, res) => {
    res.status(201).json({ message: req.i18n('project_created'), project: req.body });
  }
);

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
