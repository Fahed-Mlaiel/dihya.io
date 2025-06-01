/**
 * Hotellerie API Routes
 * RESTful & GraphQL endpoints for hotel project management
 * Sécurité maximale, i18n, multitenancy, plugins, fallback IA, audit, SEO, RGPD
 * @module routes/hotellerie
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
  type Reservation { id: ID!, client: String!, chambre: String!, date: String! }
  type Query { reservations: [Reservation] }
  type Mutation { createReservation(client: String!, chambre: String!, date: String!): Reservation }
`);

const root = {
  reservations: async (args, context) => { return []; },
  createReservation: async ({ client, chambre, date }, context) => { return { id: '1', client, chambre, date }; }
};

router.use(i18nMiddleware(['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es']));
router.use(tenantMiddleware());
router.use(pluginMiddleware('hotellerie'));
router.use(aiFallbackMiddleware(['llama','mixtral','mistral']));
router.use(auditMiddleware('hotellerie'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());

router.post('/reservations',
  checkJwt,
  checkRole(['admin','receptionniste']),
  celebrate({ [Segments.BODY]: Joi.object({ client: Joi.string().required(), chambre: Joi.string().required(), date: Joi.string().required() }) }),
  async (req, res, next) => {
    res.status(201).json({ message: req.t('reservation_created'), data: {/*...*/} });
  }
);

router.get('/reservations',
  checkJwt,
  checkRole(['admin','receptionniste','invité']),
  async (req, res, next) => {
    res.json({ message: req.t('reservations_list'), data: [] });
  }
);

router.use('/graphql',
  checkJwt,
  graphqlHTTP({ schema, rootValue: root, graphiql: true })
);

module.exports = router;
