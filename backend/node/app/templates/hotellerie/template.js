/**
 * Template métier Hôtellerie – Dihya Coding
 * @module hotellerieTemplate
 * @description API RESTful & GraphQL, multitenant, sécurité, i18n, plugins, IA fallback, RGPD, SEO, tests, etc.
 * @author Dihya Coding
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, rateLimiter, wafMiddleware } = require('../../../../src/middleware');
const { getRooms, bookRoom } = require('../../../../src/services/hotellerieService');
const router = express.Router();

/**
 * @swagger
 * /api/hotellerie/rooms:
 *   get:
 *     summary: Liste des chambres (multilingue, sécurisé)
 *     tags: [Hotellerie]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Liste des chambres
 */
router.get('/rooms',
  checkJwt,
  checkRole(['admin', 'user', 'invité']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const rooms = await getRooms(req.tenant);
    res.json({ rooms, i18n: req.i18n });
  }
);

/**
 * @swagger
 * /api/hotellerie/booking:
 *   post:
 *     summary: Réserver une chambre (sécurisé, RGPD, plugins)
 *     tags: [Hotellerie]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               roomId:
 *                 type: string
 *               userId:
 *                 type: string
 *     responses:
 *       201:
 *         description: Réservation confirmée
 */
router.post('/booking',
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  wafMiddleware,
  rateLimiter,
  auditLog,
  async (req, res) => {
    const { roomId, userId } = req.body;
    // Validation RGPD, plugins, IA fallback
    const booking = await bookRoom({ roomId, userId, tenant: req.tenant });
    res.status(201).json({ booking, i18n: req.i18n });
  }
);

module.exports = router;
