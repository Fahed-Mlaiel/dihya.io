/**
 * Health API Routes
 * RESTful & GraphQL endpoints for health project management
 * Sécurité maximale, i18n, multitenancy, plugins, fallback IA, audit, SEO, RGPD
 * @module routes/health
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
  type Patient { id: ID!, nom: String!, age: Int!, maladie: String! }
  type Query { patients: [Patient] }
  type Mutation { createPatient(nom: String!, age: Int!, maladie: String!): Patient }
`);

const root = {
  patients: async (args, context) => { return []; },
  createPatient: async ({ nom, age, maladie }, context) => { return { id: '1', nom, age, maladie }; }
};

const pluginManager = (domain) => (req, res, next) => { next(); };

router.use(i18nMiddleware(['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es']));
router.use(tenantMiddleware());
router.use(pluginMiddleware('health'));
router.use(aiFallbackMiddleware(['llama','mixtral','mistral']));
router.use(auditMiddleware('health'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());

router.post('/patients',
  checkJwt,
  checkRole(['admin','medecin']),
  celebrate({ [Segments.BODY]: Joi.object({ nom: Joi.string().required(), age: Joi.number().required(), maladie: Joi.string().required() }) }),
  async (req, res, next) => {
    res.status(201).json({ message: req.t('patient_created'), data: {/*...*/} });
  }
);

router.get('/patients',
  checkJwt,
  checkRole(['admin','medecin','invité']),
  async (req, res, next) => {
    res.json({ message: req.t('patients_list'), data: [] });
  }
);

router.get('/health', (req, res) => res.status(200).json({ status: 'ok' }));

router.use('/graphql',
  checkJwt,
  graphqlHTTP({ schema, rootValue: root, graphiql: true })
);

module.exports = router;
