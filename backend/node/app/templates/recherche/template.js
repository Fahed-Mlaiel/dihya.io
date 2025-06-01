/**
 * Recherche Template - Dihya
 *
 * @module recherche/template
 * @description Template REST/GraphQL pour gestion de la recherche IA/VR/AR.
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
const { generateSearchProject } = require('../../services/rechercheService');

/**
 * @route POST /api/recherche/generate
 * @desc Génère un projet de recherche IA/VR/AR
 * @access admin, user
 * @returns {object} Recherche générée
 */
router.post('/generate', checkJwt, checkRole(['admin', 'user']), i18nMiddleware, async (req, res) => {
  try {
    const { type, lang } = req.body;
    const search = await generateSearchProject(type, lang);
    res.status(201).json({ success: true, search });
  } catch (err) {
    req.auditLog('recherche_generate_error', { error: err.message });
    res.status(500).json({ success: false, error: req.t('error.internal') });
  }
});

module.exports = router;
