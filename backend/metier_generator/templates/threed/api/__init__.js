// Point d'entrée global pour toute l'API du module threed
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
