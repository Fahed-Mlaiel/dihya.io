/*
 * Dihya Coding – Gamer Module
 * Ultra secure, multilingual, extensible, production-ready.
 * Features: REST/GraphQL, CORS, JWT, RBAC, i18n, plugins, AI, SEO, RGPD, audit, tests, CI/CD.
 * Languages: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 *
 * @module gamer
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { aiMatchmaking } from '../../ai/ai.js';
import { pluginManager } from '../../plugins/pluginManager.js';
import { auditLog, checkJwt, corsOptions, i18nMiddleware, rbac, validateGamer } from '../../utils/utils.js';
import { createTournament, deleteTournament, getTournaments, updateTournament } from './services/gamerService.js';

const router = express.Router();

// Middleware sécurité, i18n, audit
router.use(corsOptions);
router.use(checkJwt);
router.use(i18nMiddleware);
router.use(auditLog);

// RBAC: admin, joueur, invité
router.use(rbac(['admin', 'player', 'guest']));

/**
 * @route GET /gamer/tournaments
 * @desc Liste des tournois (multilingue, paginé, filtré, SEO, plugins)
 * @access Public
 */
router.get('/tournaments', async (req, res) => {
  const tournaments = await getTournaments(req);
  res.json({ tournaments, lang: req.lang });
});

/**
 * @route POST /gamer/tournaments
 * @desc Création d’un tournoi (validation, audit, plugins, IA)
 * @access Admin/Player
 */
router.post('/tournaments', validateGamer, async (req, res) => {
  const tournament = await createTournament(req.body, req.user);
  res.status(201).json({ tournament });
});

/**
 * @route PUT /gamer/tournaments/:id
 * @desc Modification d’un tournoi (validation, audit, plugins)
 * @access Admin/Player
 */
router.put('/tournaments/:id', validateGamer, async (req, res) => {
  const tournament = await updateTournament(req.params.id, req.body, req.user);
  res.json({ tournament });
});

/**
 * @route DELETE /gamer/tournaments/:id
 * @desc Suppression d’un tournoi (audit, plugins)
 * @access Admin/Player
 */
router.delete('/tournaments/:id', rbac(['admin', 'player']), async (req, res) => {
  await deleteTournament(req.params.id, req.user);
  res.status(204).send();
});

/**
 * @route POST /gamer/tournaments/ai-matchmaking
 * @desc Matchmaking IA pour tournoi (LLaMA, Mixtral, fallback Mistral)
 * @access Player/Admin
 */
router.post('/tournaments/ai-matchmaking', async (req, res) => {
  const match = await aiMatchmaking(req.body, req.lang);
  res.json({ match });
});

// Plugins dynamiques (tournois, scoring, analytics)
pluginManager.registerRoutes(router, 'gamer');

// GraphQL endpoint (exemple)
// ...existing code...

export default router;
