/**
 * Assurance API Routes
 * RESTful & GraphQL endpoints for insurance project management
 * Sécurité maximale, i18n, multitenancy, plugins, fallback IA, audit, SEO, RGPD
 * @module routes/assurance
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
  type Contrat { id: ID!, assure: String!, type: String!, montant: Float! }
  type Query { contrats: [Contrat] }
  type Mutation { createContrat(assure: String!, type: String!, montant: Float!): Contrat }
`);

const root = {
  contrats: async (args, context) => { return []; },
  createContrat: async ({ assure, type, montant }, context) => { return { id: '1', assure, type, montant }; }
};

router.use(i18nMiddleware(['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es']));
router.use(tenantMiddleware());
router.use(pluginMiddleware('assurance'));
router.use(aiFallbackMiddleware(['llama','mixtral','mistral']));
router.use(auditMiddleware('assurance'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());

router.post('/contrats',
  checkJwt,
  checkRole(['admin','agent']),
  celebrate({ [Segments.BODY]: Joi.object({ assure: Joi.string().required(), type: Joi.string().required(), montant: Joi.number().required() }) }),
  async (req, res, next) => {
    res.status(201).json({ message: req.t('contrat_created'), data: {/*...*/} });
  }
);

router.get('/contrats',
  checkJwt,
  checkRole(['admin','agent','invité']),
  async (req, res, next) => {
    res.json({ message: req.t('contrats_list'), data: [] });
  }
);

router.use('/graphql',
  checkJwt,
  graphqlHTTP({ schema, rootValue: root, graphiql: true })
);

module.exports = router;
