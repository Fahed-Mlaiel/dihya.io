/**
 * Immobilier API Routes
 * RESTful & GraphQL endpoints for real estate project management
 * Sécurité maximale, i18n, multitenancy, plugins, fallback IA, audit, SEO, RGPD
 * @module routes/immobilier
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
  type Bien { id: ID!, adresse: String!, type: String!, prix: Float! }
  type Query { biens: [Bien] }
  type Mutation { createBien(adresse: String!, type: String!, prix: Float!): Bien }
`);

const root = {
  biens: async (args, context) => { return []; },
  createBien: async ({ adresse, type, prix }, context) => { return { id: '1', adresse, type, prix }; }
};

router.use(i18nMiddleware(['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es']));
router.use(tenantMiddleware());
router.use(pluginMiddleware('immobilier'));
router.use(aiFallbackMiddleware(['llama','mixtral','mistral']));
router.use(auditMiddleware('immobilier'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());

router.post('/biens',
  checkJwt,
  checkRole(['admin','agent']),
  celebrate({ [Segments.BODY]: Joi.object({ adresse: Joi.string().required(), type: Joi.string().required(), prix: Joi.number().required() }) }),
  async (req, res, next) => {
    res.status(201).json({ message: req.t('bien_created'), data: {/*...*/} });
  }
);

router.get('/biens',
  checkJwt,
  checkRole(['admin','agent','invité']),
  async (req, res, next) => {
    res.json({ message: req.t('biens_list'), data: [] });
  }
);

router.use('/graphql',
  checkJwt,
  graphqlHTTP({ schema, rootValue: root, graphiql: true })
);

module.exports = router;
