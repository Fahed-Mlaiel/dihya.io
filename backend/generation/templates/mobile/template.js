// Template de génération avancée d'applications mobiles pour Dihya Coding.
// RESTful, GraphQL, sécurité maximale, multilingue, extensible.

/**
 * Gestion de la génération d'applications mobiles (React Native, Flutter, PWA)
 * @module mobile
 * @see policy.md pour la politique complète
 */
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, wafMiddleware } = require('../../../../middlewares/security');
const { generateMobileApp, getMobileApp, listMobileApps, deleteMobileApp } = require('../../../../services/mobile');
const router = express.Router();

/**
 * @swagger
 * /api/mobile/generate:
 *   post:
 *     summary: Générer une application mobile
 *     security: [BearerAuth]
 *     tags: [Mobile]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               projectName:
 *                 type: string
 *               platform:
 *                 type: string
 *                 enum: [ios, android, cross, pwa]
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
  generateMobileApp
);

router.get('/:id',
  wafMiddleware,
  checkJwt,
  i18nMiddleware,
  auditLog,
  getMobileApp
);

router.get('/',
  wafMiddleware,
  checkJwt,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  listMobileApps
);

router.delete('/:id',
  wafMiddleware,
  checkJwt,
  checkRole(['admin']),
  i18nMiddleware,
  auditLog,
  deleteMobileApp
);

module.exports = router;
