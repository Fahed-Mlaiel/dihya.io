// Index clé en main pour tous les middlewares du module threed

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

// Utilisation :
// const middlewares = require('./middlewares');
// app.use(middlewares.threedSession);
// app.use(middlewares.threedLogger);
// app.use(middlewares.threedAuth);
// app.use(middlewares.threedInput);
