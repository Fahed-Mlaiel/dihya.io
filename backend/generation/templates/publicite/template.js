// Template de gestion avancée de la publicité pour Dihya Coding.
// RESTful, GraphQL, sécurité maximale, multilingue, extensible.

/**
 * Gestion de la publicité dynamique (web, mobile, VR/AR, IA)
 * @module publicite
 * @see policy.md pour la politique complète
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, wafMiddleware } = require('../../../../middlewares/security');
const { createAd, getAd, listAds, deleteAd } = require('../../../../services/publicite');
const router = express.Router();

/**
 * @swagger
 * /api/publicite/create:
 *   post:
 *     summary: Créer une publicité
 *     security: [BearerAuth]
 *     tags: [Publicite]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               content:
 *                 type: string
 *               cible:
 *                 type: string
 *     responses:
 *       200:
 *         description: Succès
 *       400:
 *         description: Erreur de validation
 *       401:
 *         description: Non autorisé
 */
router.post('/create',
  wafMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  createAd
);

router.get('/:id',
  wafMiddleware,
  checkJwt,
  i18nMiddleware,
  auditLog,
  getAd
);

router.get('/',
  wafMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  listAds
);

router.delete('/:id',
  wafMiddleware,
  checkJwt,
  checkRole(['admin']),
  i18nMiddleware,
  auditLog,
  deleteAd
);

module.exports = router;
