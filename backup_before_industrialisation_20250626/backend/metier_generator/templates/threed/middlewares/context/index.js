// Index clé en main pour tous les middlewares de contexte du module threed

const session = require('./session');
const trace = require('./trace');

module.exports = {
  ...session,
  ...trace
};

// Utilisation :
// const context = require('./context');
// app.use(context.threedSession);
// app.use(context.threedTrace);
