// Point d'entrée global pour tous les tests centralisés threed
const fs = require('fs');
const path = require('path');
function loadModules(dir) {
  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      loadModules(fullPath);
    } else if (file.endsWith('.js') && file !== '__init__.js') {
      require(fullPath);
    }
  });
}
loadModules(__dirname);

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
