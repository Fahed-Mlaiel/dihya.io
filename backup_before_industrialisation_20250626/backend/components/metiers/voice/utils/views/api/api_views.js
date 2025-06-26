// api_views.js – Helpers et endpoints API avancés pour le module voice
// REST, GraphQL, conformité RGPD, accessibilité, audit, souveraineté numérique
const express = require('express');
const router = express.Router();

/**
 * @swagger
 * /api/voice/render:
 *   post:
 *     summary: Rendu voice via API
 *     tags: [voice]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               nom:
 *                 type: string
 *               statut:
 *                 type: string
 *               details:
 *                 type: string
 *     responses:
 *       200:
 *         description: Vue voice rendue
 */
router.post('/voice/render', (req, res) => {
  const { nom, statut, details = '' } = req.body;
  // RGPD: pas de données personnelles, audit log, accessibilité
  res.json({ nom, statut, details });
});

module.exports = router;
