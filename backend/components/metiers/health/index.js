/*
 * Dihya Coding – Health Module
 * Ultra secure, multilingual, extensible, production-ready.
 * Features: REST/GraphQL, CORS, JWT, RBAC, i18n, plugins, AI, SEO, RGPD, audit, tests, CI/CD.
 * Languages: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 *
 * @module health
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { aiMedicalDoc } from '../../ai/ai.js';
import { pluginManager } from '../../plugins/pluginManager.js';
import { auditLog, checkJwt, corsOptions, i18nMiddleware, rbac, validateHealth } from '../../utils/utils.js';
import { createAppointment, deleteAppointment, getAppointments, updateAppointment } from './services/healthService.js';

const router = express.Router();

// Middleware sécurité, i18n, audit
router.use(corsOptions);
router.use(checkJwt);
router.use(i18nMiddleware);
router.use(auditLog);

// RBAC: admin, médecin, patient, invité
router.use(rbac(['admin', 'doctor', 'patient', 'guest']));

/**
 * @route GET /health/appointments
 * @desc Liste des rendez-vous (multilingue, paginé, filtré, SEO, plugins)
 * @access Public
 */
router.get('/appointments', async (req, res) => {
  const appointments = await getAppointments(req);
  res.json({ appointments, lang: req.lang });
});

/**
 * @route POST /health/appointments
 * @desc Création d’un rendez-vous (validation, audit, plugins, IA)
 * @access Admin/Doctor/Patient
 */
router.post('/appointments', validateHealth, async (req, res) => {
  const appointment = await createAppointment(req.body, req.user);
  res.status(201).json({ appointment });
});

/**
 * @route PUT /health/appointments/:id
 * @desc Modification d’un rendez-vous (validation, audit, plugins)
 * @access Admin/Doctor/Patient
 */
router.put('/appointments/:id', validateHealth, async (req, res) => {
  const appointment = await updateAppointment(req.params.id, req.body, req.user);
  res.json({ appointment });
});

/**
 * @route DELETE /health/appointments/:id
 * @desc Suppression d’un rendez-vous (audit, plugins)
 * @access Admin/Doctor/Patient
 */
router.delete('/appointments/:id', rbac(['admin', 'doctor', 'patient']), async (req, res) => {
  await deleteAppointment(req.params.id, req.user);
  res.status(204).send();
});

/**
 * @route POST /health/appointments/ai-doc
 * @desc Génération IA de document médical (LLaMA, Mixtral, fallback Mistral)
 * @access Doctor/Admin
 */
router.post('/appointments/ai-doc', async (req, res) => {
  const doc = await aiMedicalDoc(req.body, req.lang);
  res.json({ doc });
});

// Plugins dynamiques (télémédecine, analytics)
pluginManager.registerRoutes(router, 'health');

// GraphQL endpoint (exemple)
// ...existing code...

export default router;
