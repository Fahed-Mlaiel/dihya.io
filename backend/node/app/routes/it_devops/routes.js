/**
 * IT/DevOps API Routes
 * RESTful & GraphQL endpoints for IT/DevOps project management
 * Sécurité maximale, i18n, multitenancy, plugins, fallback IA, audit, SEO, RGPD
 * @module routes/it_devops
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
  type Pipeline { id: ID!, nom: String!, type: String!, status: String! }
  type Query { pipelines: [Pipeline] }
  type Mutation { createPipeline(nom: String!, type: String!, status: String!): Pipeline }
`);

const root = {
  pipelines: async (args, context) => { return []; },
  createPipeline: async ({ nom, type, status }, context) => { return { id: '1', nom, type, status }; }
};

router.use(i18nMiddleware(['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es']));
router.use(tenantMiddleware());
router.use(pluginMiddleware('it_devops'));
router.use(aiFallbackMiddleware(['llama','mixtral','mistral']));
router.use(auditMiddleware('it_devops'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());

router.post('/pipelines',
  checkJwt,
  checkRole(['admin','devops']),
  celebrate({ [Segments.BODY]: Joi.object({ nom: Joi.string().required(), type: Joi.string().required(), status: Joi.string().required() }) }),
  async (req, res, next) => {
    res.status(201).json({ message: req.t('pipeline_created'), data: {/*...*/} });
  }
);

router.get('/pipelines',
  checkJwt,
  checkRole(['admin','devops','invité']),
  async (req, res, next) => {
    res.json({ message: req.t('pipelines_list'), data: [] });
  }
);

router.use('/graphql',
  checkJwt,
  graphqlHTTP({ schema, rootValue: root, graphiql: true })
);

module.exports = router;
