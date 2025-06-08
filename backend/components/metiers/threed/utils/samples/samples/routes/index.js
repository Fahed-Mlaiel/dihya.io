// index.js - Exécution centralisée des routes samples
const handlers = require('./handlers');
const middlewares = require('./middlewares');
const samples = require('./samples');
module.exports = { handlers, middlewares, samples };
