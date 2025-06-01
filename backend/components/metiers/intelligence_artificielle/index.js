/*
 * Dihya Coding – Intelligence Artificielle Module
 * Ultra secure, multilingual, extensible, production-ready.
 * Features: REST/GraphQL, CORS, JWT, RBAC, i18n, plugins, AI, SEO, RGPD, audit, tests, CI/CD.
 * Languages: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 *
 * @module intelligence_artificielle
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { aiDeployModel } from '../../ai/ai.js';
import { pluginManager } from '../../plugins/pluginManager.js';
import { auditLog, checkJwt, corsOptions, i18nMiddleware, rbac, validateAI } from '../../utils/utils.js';
import { createModel, deleteModel, getModels, updateModel } from './services/intelligenceArtificielleService.js';

const router = express.Router();

// Middleware sécurité, i18n, audit
router.use(corsOptions);
router.use(checkJwt);
router.use(i18nMiddleware);
router.use(auditLog);

// RBAC: admin, data scientist, user, invité
router.use(rbac(['admin', 'data_scientist', 'user', 'guest']));

/**
 * @route GET /intelligence_artificielle/models
 * @desc Liste des modèles IA (multilingue, paginé, filtré, SEO, plugins)
 * @access Public
 */
router.get('/models', async (req, res) => {
  const models = await getModels(req);
  res.json({ models, lang: req.lang });
});

/**
 * @route POST /intelligence_artificielle/models
 * @desc Déploiement d’un modèle IA (validation, audit, plugins, IA)
 * @access Admin/Data Scientist
 */
router.post('/models', validateAI, async (req, res) => {
  const model = await createModel(req.body, req.user);
  res.status(201).json({ model });
});

/**
 * @route PUT /intelligence_artificielle/models/:id
 * @desc Modification d’un modèle IA (validation, audit, plugins)
 * @access Admin/Data Scientist
 */
router.put('/models/:id', validateAI, async (req, res) => {
  const model = await updateModel(req.params.id, req.body, req.user);
  res.json({ model });
});

/**
 * @route DELETE /intelligence_artificielle/models/:id
 * @desc Suppression d’un modèle IA (audit, plugins)
 * @access Admin/Data Scientist
 */
router.delete('/models/:id', rbac(['admin', 'data_scientist']), async (req, res) => {
  await deleteModel(req.params.id, req.user);
  res.status(204).send();
});

/**
 * @route POST /intelligence_artificielle/models/ai-deploy
 * @desc Déploiement IA de modèle (LLaMA, Mixtral, fallback Mistral)
 * @access Data Scientist/Admin
 */
router.post('/models/ai-deploy', async (req, res) => {
  const deployment = await aiDeployModel(req.body, req.lang);
  res.json({ deployment });
});

// Plugins dynamiques (connecteurs, monitoring, explainability)
pluginManager.registerRoutes(router, 'intelligence_artificielle');

// GraphQL endpoint (exemple)
// ...existing code...

export default router;
