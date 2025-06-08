// index.js - Exécution centralisée des samples de routes imbriqués
const handlers = require('./handlers');
const middlewares = require('./middlewares');
const samples = require('./samples');
module.exports = { handlers, middlewares, samples };
