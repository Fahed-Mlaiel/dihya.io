// Template de gestion avancée de la recherche pour Dihya Coding.
// RESTful, GraphQL, sécurité maximale, multilingue, extensible.

/**
 * Gestion de la recherche avancée (web, mobile, IA, VR/AR)
 * @module recherche
 * @see policy.md pour la politique complète
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, wafMiddleware } = require('../../../../middlewares/security');
const { queryRecherche, getRecherche, listRecherches, deleteRecherche } = require('../../../../services/recherche');
const router = express.Router();

/**
 * @swagger
 * /api/recherche/query:
 *   post:
 *     summary: Effectuer une recherche avancée
 *     security: [BearerAuth]
 *     tags: [Recherche]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               query:
 *                 type: string
 *               filters:
 *                 type: object
 *     responses:
 *       200:
 *         description: Succès
 *       400:
 *         description: Erreur de validation
 *       401:
 *         description: Non autorisé
 */
router.post('/query',
  wafMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  queryRecherche
);

router.get('/:id',
  wafMiddleware,
  checkJwt,
  i18nMiddleware,
  auditLog,
  getRecherche
);

router.get('/',
  wafMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  listRecherches
);

router.delete('/:id',
  wafMiddleware,
  checkJwt,
  checkRole(['admin']),
  i18nMiddleware,
  auditLog,
  deleteRecherche
);

module.exports = router;
