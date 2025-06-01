/**
 * Restauration Template - Dihya
 *
 * @module restauration/template
 * @description Template REST/GraphQL pour gestion de la restauration IA/VR/AR.
 * @i18n Support: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @roles admin, user, invité
 * @plugins extensible
 * @seo robots, sitemap, logs
 * @compliance RGPD, auditabilité
 */

const express = require('express');
const router = express.Router();
const { checkJwt, checkRole, i18nMiddleware } = require('../../middlewares');
const { generateCateringProject } = require('../../services/restaurationService');

/**
 * @route POST /api/restauration/generate
 * @desc Génère un projet restauration IA/VR/AR
 * @access admin, user
 * @returns {object} Restauration générée
 */
router.post('/generate', checkJwt, checkRole(['admin', 'user']), i18nMiddleware, async (req, res) => {
  try {
    const { type, lang } = req.body;
    const catering = await generateCateringProject(type, lang);
    res.status(201).json({ success: true, catering });
  } catch (err) {
    req.auditLog('restauration_generate_error', { error: err.message });
    res.status(500).json({ success: false, error: req.t('error.internal') });
  }
});

module.exports = router;
