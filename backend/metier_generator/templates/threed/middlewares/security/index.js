// Index clé en main pour tous les middlewares de sécurité du module threed

const audit = require('./audit');
const auth = require('./auth');

module.exports = {
  ...audit,
  ...auth
};

// Utilisation :
// const security = require('./security');
// app.use(security.threedAudit);
// app.use(security.threedAuth);
