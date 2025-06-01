/**
 * @file template.js
 * @description Template avancé pour la gestion de projets "VR/AR" (web, mobile, IA, VR, AR) dans Dihya Coding.
 * @author Dihya Team
 * @version 1.0.0
 * @license MIT
 *
 * Sécurité : JWT, CORS, audit, WAF, anti-DDOS.
 * Multilingue : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
 * RGPD, auditabilité, anonymisation, export.
 */

const { Router } = require('express');
const { checkJWT, checkRole, i18nMiddleware, auditLog } = require('../../../../middlewares');
const { createVRAR, listVRAR } = require('../../../../services/vrArService');

/**
 * @swagger
 * /api/vr_ar:
 *   post:
 *     summary: Créer un projet VR/AR
 *     tags: [VR/AR]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               name:
 *                 type: string
 *               description:
 *                 type: string
 *               lang:
 *                 type: string
 *               tenant:
 *                 type: string
 *     responses:
 *       201:
 *         description: Projet créé
 *       400:
 *         description: Erreur de validation
 *       401:
 *         description: Non autorisé
 */
const router = Router();

router.post(
  '/',
  checkJWT,
  checkRole(['admin', 'user']),
  i18nMiddleware,
  auditLog,
  async (req, res) => {
    try {
      const { name, description, lang, tenant } = req.body;
      if (!name || !lang || !tenant) {
        return res.status(400).json({ error: req.t('missing_fields') });
      }
      const project = await createVRAR({ name, description, lang, tenant });
      res.status(201).json(project);
    } catch (err) {
      res.status(500).json({ error: req.t('internal_error') });
    }
  }
);

router.get(
  '/',
  checkJWT,
  checkRole(['admin', 'user', 'invite']),
  i18nMiddleware,
  auditLog,
  async (req, res) => {
    try {
      const projects = await listVRAR(req.user, req.tenant);
      res.status(200).json(projects);
    } catch (err) {
      res.status(500).json({ error: req.t('internal_error') });
    }
  }
);

module.exports = router;
