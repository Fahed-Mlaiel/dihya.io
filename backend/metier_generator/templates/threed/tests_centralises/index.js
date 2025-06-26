// Index clé en main pour tous les tests centralisés threed

const api = require('./api');
const devops = require('./devops');
const docs = require('./docs');
const hooks = require('./hooks');
const i18n = require('./i18n');
const middlewares = require('./middlewares');
const models = require('./models');
const plugins = require('./plugins');
const security = require('./security');
const services = require('./services');
const validations = require('./validations');

module.exports = {
  ...api,
  ...devops,
  ...docs,
  ...hooks,
  ...i18n,
  ...middlewares,
  ...models,
  ...plugins,
  ...security,
  ...services,
  ...validations
};

// Utilisation :
// const tests = require('./tests_centralises');
// tests.testThreedAssetValidation(...);
// tests.testSession(...);
// tests.testApi(...);
