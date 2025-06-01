// Template de gestion avancée des médias pour Dihya Coding.
// RESTful, GraphQL, sécurité maximale, multilingue, extensible.

/**
 * Gestion des médias (upload, transformation, diffusion)
 * @module medias
 * @see policy.md pour la politique complète
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, wafMiddleware } = require('../../../../middlewares/security');
const { uploadMedia, getMedia, listMedias, deleteMedia } = require('../../../../services/medias');
const router = express.Router();

/**
 * @swagger
 * /api/medias/upload:
 *   post:
 *     summary: Upload d’un média
 *     security: [BearerAuth]
 *     tags: [Medias]
 *     requestBody:
 *       required: true
 *       content:
 *         multipart/form-data:
 *           schema:
 *             type: object
 *             properties:
 *               file:
 *                 type: string
 *                 format: binary
 *     responses:
 *       200:
 *         description: Succès
 *       400:
 *         description: Erreur de validation
 *       401:
 *         description: Non autorisé
 */
router.post('/upload',
  wafMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  uploadMedia
);

/**
 * @swagger
 * /api/medias/:id:
 *   get:
 *     summary: Récupérer un média
 *     security: [BearerAuth]
 *     tags: [Medias]
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: Succès
 *       404:
 *         description: Non trouvé
 */
router.get('/:id',
  wafMiddleware,
  checkJwt,
  i18nMiddleware,
  auditLog,
  getMedia
);

router.get('/',
  wafMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  listMedias
);

router.delete('/:id',
  wafMiddleware,
  checkJwt,
  checkRole(['admin']),
  i18nMiddleware,
  auditLog,
  deleteMedia
);

module.exports = router;
