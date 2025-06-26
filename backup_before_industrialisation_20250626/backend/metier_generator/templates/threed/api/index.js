// Index clé en main pour toute l'API du module threed

const controllers = require('./controllers');
const docs = require('./docs');
const middlewares = require('./middlewares');
const pagination = require('./pagination');
const routes = require('./routes');
const versioning = require('./versioning');

module.exports = {
  ...controllers,
  ...docs,
  ...middlewares,
  ...pagination,
  ...routes,
  ...versioning
};

// Utilisation :
// const api = require('./api');
// api.assetController.create(...);
// api.assetRoutes(app);
// api.loggerMiddleware(...);
// api.paginationMiddleware(...);
// api.versioningMiddleware(...);
