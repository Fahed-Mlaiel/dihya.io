// Index clé en main pour tous les middlewares de validation du module threed

const input = require('./input');
const schema = require('./schema');

module.exports = {
  ...input,
  ...schema
};

// Utilisation :
// const validation = require('./validation');
// app.use(validation.threedInput);
// app.use(validation.threedSchema);
