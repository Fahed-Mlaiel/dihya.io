/**
 * Construction API Routes
 * RESTful & GraphQL endpoints for construction project management
 * Sécurité maximale, i18n, multitenancy, plugins, fallback IA, audit, SEO, RGPD
 * @module routes/construction
 * @author Dihya Team
 * @since 2025-05-25
 */

const express = require('express');
const { celebrate, Joi, Segments } = require('celebrate');
const { checkJwt, checkRole, i18nMiddleware, tenantMiddleware, pluginMiddleware, aiFallbackMiddleware, auditMiddleware, seoMiddleware, rgpdMiddleware } = require('../../middlewares/global');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');
const router = express.Router();

const schema = buildSchema(`
  type Projet { id: ID!, nom: String!, type: String!, budget: Float! }
  type Query { projets: [Projet] }
  type Mutation { createProjet(nom: String!, type: String!, budget: Float!): Projet }
`);

const root = {
  projets: async (args, context) => { return []; },
  createProjet: async ({ nom, type, budget }, context) => { return { id: '1', nom, type, budget }; }
};

router.use(i18nMiddleware(['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es']));
router.use(tenantMiddleware());
router.use(pluginMiddleware('construction'));
router.use(aiFallbackMiddleware(['llama','mixtral','mistral']));
router.use(auditMiddleware('construction'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());

router.post('/projets',
  checkJwt,
  checkRole(['admin','chefprojet']),
  celebrate({ [Segments.BODY]: Joi.object({ nom: Joi.string().required(), type: Joi.string().required(), budget: Joi.number().required() }) }),
  async (req, res, next) => {
    res.status(201).json({ message: req.t('projet_created'), data: {/*...*/} });
  }
);

router.get('/projets',
  checkJwt,
  checkRole(['admin','chefprojet','invité']),
  async (req, res, next) => {
    res.json({ message: req.t('projets_list'), data: [] });
  }
);

router.use('/graphql',
  checkJwt,
  graphqlHTTP({ schema, rootValue: root, graphiql: true })
);

module.exports = router;
