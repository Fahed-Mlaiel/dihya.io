// Template de gestion avancée des previews pour Dihya Coding.
// RESTful, GraphQL, sécurité maximale, multilingue, extensible.

/**
 * Gestion des previews dynamiques (web, mobile, VR/AR, IA)
 * @module preview
 * @see policy.md pour la politique complète
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, wafMiddleware } = require('../../../../middlewares/security');
const { generatePreview, getPreview, listPreviews, deletePreview } = require('../../../../services/preview');
const router = express.Router();

/**
 * @swagger
 * /api/preview/generate:
 *   post:
 *     summary: Générer une preview
 *     security: [BearerAuth]
 *     tags: [Preview]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               source:
 *                 type: string
 *               type:
 *                 type: string
 *                 enum: [web, mobile, vr, ar, ia]
 *     responses:
 *       200:
 *         description: Succès
 *       400:
 *         description: Erreur de validation
 *       401:
 *         description: Non autorisé
 */
router.post('/generate',
  wafMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  generatePreview
);

router.get('/:id',
  wafMiddleware,
  checkJwt,
  i18nMiddleware,
  auditLog,
  getPreview
);

router.get('/',
  wafMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  listPreviews
);

router.delete('/:id',
  wafMiddleware,
  checkJwt,
  checkRole(['admin']),
  i18nMiddleware,
  auditLog,
  deletePreview
);

module.exports = router;
