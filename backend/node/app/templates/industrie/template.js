/**
 * Template métier Industrie – Dihya Coding
 * @module industrieTemplate
 * @description API RESTful & GraphQL, multitenant, sécurité, i18n, plugins, IA fallback, RGPD, SEO, tests, etc.
 * @author Dihya Coding
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, rateLimiter, wafMiddleware } = require('../../../../src/middleware');
const { getMachines, declareMaintenance } = require('../../../../src/services/industrieService');
const router = express.Router();

/**
 * @swagger
 * /api/industrie/machines:
 *   get:
 *     summary: Liste des machines (multilingue, sécurisé)
 *     tags: [Industrie]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Liste des machines
 */
router.get('/machines',
  checkJwt,
  checkRole(['admin', 'opérateur', 'technicien', 'invité']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const machines = await getMachines(req.tenant);
    res.json({ machines, i18n: req.i18n });
  }
);

/**
 * @swagger
 * /api/industrie/maintenance:
 *   post:
 *     summary: Déclarer une maintenance (sécurisé, RGPD, plugins)
 *     tags: [Industrie]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               machineId:
 *                 type: string
 *               technicianId:
 *                 type: string
 *               description:
 *                 type: string
 *     responses:
 *       201:
 *         description: Maintenance déclarée
 */
router.post('/maintenance',
  checkJwt,
  checkRole(['admin', 'technicien']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const { machineId, technicianId, description } = req.body;
    // Validation RGPD, plugins, IA fallback
    const result = await declareMaintenance({ machineId, technicianId, description, tenant: req.tenant });
    res.status(201).json({ result, i18n: req.i18n });
  }
);

module.exports = router;
