/**
 * Publicité Template - Dihya
 *
 * @module publicite/template
 * @description Template REST/GraphQL pour gestion des publicités IA/VR/AR.
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
const { generateAdvertisingProject } = require('../../services/publiciteService');

/**
 * @route POST /api/publicite/generate
 * @desc Génère une publicité IA/VR/AR
 * @access admin, user
 * @returns {object} Publicité générée
 */
router.post('/generate', checkJwt, checkRole(['admin', 'user']), i18nMiddleware, async (req, res) => {
  try {
    const { type, lang } = req.body;
    const advertising = await generateAdvertisingProject(type, lang);
    res.status(201).json({ success: true, advertising });
  } catch (err) {
    req.auditLog('publicite_generate_error', { error: err.message });
    res.status(500).json({ success: false, error: req.t('error.internal') });
  }
});

module.exports = router;
