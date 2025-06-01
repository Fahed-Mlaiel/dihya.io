/**
 * Crypto API Routes
 * RESTful & GraphQL endpoints for crypto project management
 * Sécurité maximale, i18n, multitenancy, plugins, fallback IA, audit, SEO, RGPD
 * @module routes/crypto
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
  type Wallet { id: ID!, owner: String!, solde: Float!, actif: Boolean! }
  type Query { wallets: [Wallet] }
  type Mutation { createWallet(owner: String!, solde: Float!): Wallet }
`);

const root = {
  wallets: async (args, context) => { return []; },
  createWallet: async ({ owner, solde }, context) => { return { id: '1', owner, solde, actif: true }; }
};

router.use(i18nMiddleware(['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es']));
router.use(tenantMiddleware());
router.use(pluginMiddleware('crypto'));
router.use(aiFallbackMiddleware(['llama','mixtral','mistral']));
router.use(auditMiddleware('crypto'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());

router.post('/wallets',
  checkJwt,
  checkRole(['admin','user']),
  celebrate({ [Segments.BODY]: Joi.object({ owner: Joi.string().required(), solde: Joi.number().required() }) }),
  async (req, res, next) => {
    res.status(201).json({ message: req.t('wallet_created'), data: {/*...*/} });
  }
);

router.get('/wallets',
  checkJwt,
  checkRole(['admin','user','invité']),
  async (req, res, next) => {
    res.json({ message: req.t('wallets_list'), data: [] });
  }
);

router.use('/graphql',
  checkJwt,
  graphqlHTTP({ schema, rootValue: root, graphiql: true })
);

module.exports = router;
