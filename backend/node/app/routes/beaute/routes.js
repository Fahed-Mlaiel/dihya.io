/**
 * Beauté API Routes
 * RESTful & GraphQL endpoints for beauty project management
 * Sécurité maximale, i18n, multitenancy, plugins, fallback IA, audit, SEO, RGPD
 * @module routes/beaute
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
  type Soin { id: ID!, nom: String!, type: String!, prix: Float! }
  type Query { soins: [Soin] }
  type Mutation { createSoin(nom: String!, type: String!, prix: Float!): Soin }
`);

const root = {
  soins: async (args, context) => { return []; },
  createSoin: async ({ nom, type, prix }, context) => { return { id: '1', nom, type, prix }; }
};

router.use(i18nMiddleware(['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es']));
router.use(tenantMiddleware());
router.use(pluginMiddleware('beaute'));
router.use(aiFallbackMiddleware(['llama','mixtral','mistral']));
router.use(auditMiddleware('beaute'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());

router.post('/soins',
  checkJwt,
  checkRole(['admin','estheticienne']),
  celebrate({ [Segments.BODY]: Joi.object({ nom: Joi.string().required(), type: Joi.string().required(), prix: Joi.number().required() }) }),
  async (req, res, next) => {
    res.status(201).json({ message: req.t('soin_created'), data: {/*...*/} });
  }
);

router.get('/soins',
  checkJwt,
  checkRole(['admin','estheticienne','invité']),
  async (req, res, next) => {
    res.json({ message: req.t('soins_list'), data: [] });
  }
);

router.use('/graphql',
  checkJwt,
  graphqlHTTP({ schema, rootValue: root, graphiql: true })
);

module.exports = router;
