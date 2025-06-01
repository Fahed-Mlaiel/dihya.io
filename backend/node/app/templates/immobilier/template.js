/**
 * Template métier Immobilier – Dihya Coding
 * @module immobilierTemplate
 * @description API RESTful & GraphQL, multitenant, sécurité, i18n, plugins, IA fallback, RGPD, SEO, tests, etc.
 * @author Dihya Coding
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, rateLimiter, wafMiddleware } = require('../../../../src/middleware');
const { getProperties, submitOffer } = require('../../../../src/services/immobilierService');
const router = express.Router();

/**
 * @swagger
 * /api/immobilier/properties:
 *   get:
 *     summary: Liste des biens immobiliers (multilingue, sécurisé)
 *     tags: [Immobilier]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Liste des biens
 */
router.get('/properties',
  checkJwt,
  checkRole(['admin', 'agent', 'client', 'invité']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const properties = await getProperties(req.tenant);
    res.json({ properties, i18n: req.i18n });
  }
);

/**
 * @swagger
 * /api/immobilier/offer:
 *   post:
 *     summary: Soumettre une offre (sécurisé, RGPD, plugins)
 *     tags: [Immobilier]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               propertyId:
 *                 type: string
 *               clientId:
 *                 type: string
 *               offer:
 *                 type: number
 *     responses:
 *       201:
 *         description: Offre soumise
 */
router.post('/offer',
  checkJwt,
  checkRole(['admin', 'agent', 'client']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const { propertyId, clientId, offer } = req.body;
    // Validation RGPD, plugins, IA fallback
    const result = await submitOffer({ propertyId, clientId, offer, tenant: req.tenant });
    res.status(201).json({ result, i18n: req.i18n });
  }
);

module.exports = router;
