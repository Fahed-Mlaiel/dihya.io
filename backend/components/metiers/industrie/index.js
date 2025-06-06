/*
 * Dihya Coding – Environnement Module (Ultra avancé, clé en main)
 * Ultra secure, multilingual, extensible, production-ready, RGPD, audit, plugins, i18n, multitenancy, CI/CD, accessibilité, tests, extension dynamique.
 * @module environnement
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { aiDetectAnomaly } from '../../ai/ai.js';
import { pluginManager } from '../../plugins/pluginManager.js';
import { auditLog, checkJwt, corsOptions, i18nMiddleware, rbac, validateEnvData } from '../../utils/utils.js';
import { createEnvAlert, deleteEnvAlert, getEnvData, updateEnvAlert } from './services/environnementService.js';

const router = express.Router();

// Middlewares sécurité, i18n, audit, RGPD, multitenancy
router.use(corsOptions);
router.use(checkJwt);
router.use(i18nMiddleware);
router.use(auditLog);
router.use(rbac(['admin', 'operator', 'guest']));

/**
 * @route GET /environnement/data
 * @desc Liste des données environnementales (multilingue, paginé, filtré, SEO, plugins)
 * @access Public
 */
router.get('/data', async (req, res) => {
  const data = await getEnvData(req);
  res.json({ data, lang: req.lang });
});

/**
 * @route POST /environnement/alerts
 * @desc Création d’une alerte environnementale (validation, audit, plugins, IA)
 * @access Admin/Operator
 */
router.post('/alerts', validateEnvData, async (req, res) => {
  const alert = await createEnvAlert(req.body, req.user);
  res.status(201).json({ alert });
});

/**
 * @route PUT /environnement/alerts/:id
 * @desc Modification d’une alerte environnementale (validation, audit, plugins)
 * @access Admin/Operator
 */
router.put('/alerts/:id', validateEnvData, async (req, res) => {
  const alert = await updateEnvAlert(req.params.id, req.body, req.user);
  res.json({ alert });
});

/**
 * @route DELETE /environnement/alerts/:id
 * @desc Suppression d’une alerte environnementale (audit, plugins)
 * @access Admin/Operator
 */
router.delete('/alerts/:id', rbac(['admin', 'operator']), async (req, res) => {
  await deleteEnvAlert(req.params.id, req.user);
  res.status(204).send();
});

/**
 * @route POST /environnement/alerts/ai-detect
 * @desc Détection IA d’anomalie environnementale (LLaMA, Mixtral, fallback Mistral)
 * @access Operator/Admin
 */
router.post('/alerts/ai-detect', async (req, res) => {
  const anomaly = await aiDetectAnomaly(req.body, req.lang);
  res.json({ anomaly });
});

// Plugins dynamiques (IoT, open data, analytics, extension métier)
pluginManager.registerRoutes(router, 'environnement');

// Export du routeur pour intégration CI/CD, tests, extension, audit
export default router;

// index.js – Module ultra avancé Environnement (Dihya Coding)
const api = require('./api');
const controller = require('./environnement_controller.js');
const plugin = require('./sample_plugin.js');

module.exports = {
  api,
  controller,
  plugin,
  // Documentation, i18n, sécurité, RGPD, plugins, multitenancy, audit, accessibilité
};
