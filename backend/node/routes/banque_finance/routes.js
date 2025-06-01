"use strict";
/**
 * @fileoverview Routes pour la gestion des projets Banque & Finance.
 * @module routes/banque_finance
 * @description REST & GraphQL API pour la gestion avancée des projets Banque & Finance avec sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback, etc.
 * @author Dihya Team
 * @version 1.0.0
 * @license MIT
 */

const express = require("express");
const { checkJwt, checkRole, validateBody, auditLog, i18nMiddleware, wafMiddleware, ddosMiddleware } = require("../../../../middlewares/security");
const { projectSchema } = require("../../../../schemas/project");
const { getIAFallback } = require("../../../../services/ia_fallback");
const { seoLogger } = require("../../../../middlewares/seo");
const { pluginManager } = require("../../../../plugins/pluginManager");
const router = express.Router();

/**
 * @swagger
 * /banque-finance/projects:
 *   get:
 *     summary: Liste des projets Banque & Finance
 *     tags: [BanqueFinance]
 *     security: [ { bearerAuth: [] } ]
 *     responses:
 *       200:
 *         description: Liste des projets
 */
router.get("/projects", [checkJwt, checkRole(["admin", "user"]), i18nMiddleware, wafMiddleware, ddosMiddleware, seoLogger], async (req, res) => {
  // ... récupération des projets
  res.json({ success: true, projects: [], i18n: req.i18n });
});

/**
 * @swagger
 * /banque-finance/projects:
 *   post:
 *     summary: Création d'un projet Banque & Finance
 *     tags: [BanqueFinance]
 *     security: [ { bearerAuth: [] } ]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Project'
 *     responses:
 *       201:
 *         description: Projet créé
 */
router.post("/projects", [checkJwt, checkRole(["admin"]), validateBody(projectSchema), auditLog, i18nMiddleware, wafMiddleware, ddosMiddleware, seoLogger], async (req, res) => {
  // ... création projet
  res.status(201).json({ success: true, project: req.body, i18n: req.i18n });
});

// GraphQL endpoint (exemple)
const { graphqlHTTP } = require("express-graphql");
const { banqueFinanceSchema } = require("../../../../graphql/schemas/banque_finance");
router.use("/graphql", [checkJwt, i18nMiddleware, wafMiddleware, ddosMiddleware], graphqlHTTP({
  schema: banqueFinanceSchema,
  graphiql: true,
}));

// Plugin extensibility
router.use("/plugins", pluginManager("banque_finance"));

module.exports = router;
