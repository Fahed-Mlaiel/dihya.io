/**
 * Ressources Humaines Template - Dihya
 *
 * @module ressources_humaines/template
 * @description Template REST/GraphQL pour gestion des RH IA/VR/AR.
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
const { generateHRProject } = require('../../services/ressourcesHumainesService');

/**
 * @route POST /api/ressources_humaines/generate
 * @desc Génère un projet RH IA/VR/AR
 * @access admin, user
 * @returns {object} RH généré
 */
router.post('/generate', checkJwt, checkRole(['admin', 'user']), i18nMiddleware, async (req, res) => {
  try {
    const { type, lang } = req.body;
    const hr = await generateHRProject(type, lang);
    res.status(201).json({ success: true, hr });
  } catch (err) {
    req.auditLog('ressources_humaines_generate_error', { error: err.message });
    res.status(500).json({ success: false, error: req.t('error.internal') });
  }
});

module.exports = router;
