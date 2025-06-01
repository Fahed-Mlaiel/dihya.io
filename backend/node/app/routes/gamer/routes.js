/**
 * Gamer API Routes
 * RESTful & GraphQL endpoints for gamer project management
 * Sécurité maximale, i18n, multitenancy, plugins, fallback IA, audit, SEO, RGPD
 * @module routes/gamer
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
  type Jeu { id: ID!, nom: String!, genre: String!, plateforme: String! }
  type Query { jeux: [Jeu] }
  type Mutation { createJeu(nom: String!, genre: String!, plateforme: String!): Jeu }
`);

const root = {
  jeux: async (args, context) => { return []; },
  createJeu: async ({ nom, genre, plateforme }, context) => { return { id: '1', nom, genre, plateforme }; }
};

const pluginManager = (domain) => (req, res, next) => { next(); };

router.use(i18nMiddleware(['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es']));
router.use(tenantMiddleware());
router.use(pluginMiddleware('gamer'));
router.use(aiFallbackMiddleware(['llama','mixtral','mistral']));
router.use(auditMiddleware('gamer'));
router.use(seoMiddleware());
router.use(rgpdMiddleware());

router.post('/jeux',
  checkJwt,
  checkRole(['admin','gamer']),
  celebrate({ [Segments.BODY]: Joi.object({ nom: Joi.string().required(), genre: Joi.string().required(), plateforme: Joi.string().required() }) }),
  async (req, res, next) => {
    res.status(201).json({ message: req.t('jeu_created'), data: {/*...*/} });
  }
);

router.get('/jeux',
  checkJwt,
  checkRole(['admin','gamer','invité']),
  async (req, res, next) => {
    res.json({ message: req.t('jeux_list'), data: [] });
  }
);

router.use('/graphql',
  checkJwt,
  graphqlHTTP({ schema, rootValue: root, graphiql: true })
);

module.exports = router;
