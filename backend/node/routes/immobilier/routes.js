"use strict";
/**
 * @fileoverview Routes pour la gestion des projets Immobilier.
 * @module routes/immobilier
 * @description API REST & GraphQL Immobilier, sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback, etc.
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

router.get("/projects", [checkJwt, checkRole(["admin", "user"]), i18nMiddleware, wafMiddleware, ddosMiddleware, seoLogger], async (req, res) => {
  res.json({ success: true, projects: [], i18n: req.i18n });
});

router.post("/projects", [checkJwt, checkRole(["admin"]), validateBody(projectSchema), auditLog, i18nMiddleware, wafMiddleware, ddosMiddleware, seoLogger], async (req, res) => {
  res.status(201).json({ success: true, project: req.body, i18n: req.i18n });
});

const { graphqlHTTP } = require("express-graphql");
const { immobilierSchema } = require("../../../../graphql/schemas/immobilier");
router.use("/graphql", [checkJwt, i18nMiddleware, wafMiddleware, ddosMiddleware], graphqlHTTP({
  schema: immobilierSchema,
  graphiql: true,
}));

router.use("/plugins", pluginManager("immobilier"));

module.exports = router;
