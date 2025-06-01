// Template de routes gamer avancé (REST, GraphQL, sécurité, i18n, plugins, RGPD, SEO, multitenancy, audit, IA, tests)
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginLoader } = require('../../../../core/middleware');
const { getScores, createMatch, updateMatch, deleteMatch } = require('./controller');
const router = express.Router();

router.use(i18nMiddleware);
router.use(checkJwt);
router.use(auditLog);
router.use(pluginLoader);

/**
 * @route GET /gamer/scores
 * @desc Liste des scores (multi-tenant, filtrage, pagination, i18n)
 * @access Roles: admin, joueur, invité
 */
router.get('/scores', checkRole(['admin', 'player', 'guest']), getScores);

/**
 * @route POST /gamer/match
 * @desc Création d'un match (validation, audit, RGPD)
 * @access Roles: admin, joueur
 */
router.post('/match', checkRole(['admin', 'player']), createMatch);

/**
 * @route PUT /gamer/match/:id
 * @desc Mise à jour d'un match
 * @access Roles: admin, joueur
 */
router.put('/match/:id', checkRole(['admin', 'player']), updateMatch);

/**
 * @route DELETE /gamer/match/:id
 * @desc Suppression d'un match (audit, anonymisation RGPD)
 * @access Roles: admin
 */
router.delete('/match/:id', checkRole(['admin']), deleteMatch);

module.exports = router;
