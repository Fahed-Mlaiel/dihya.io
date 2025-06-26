// Point d'entrée global pour tous les tests de middlewares threed
const context = require('./context');
const logger = require('./logger');
const security = require('./security');
const validation = require('./validation');

module.exports = {
  ...context,
  ...logger,
  ...security,
  ...validation
};
