// Index clé en main pour tous les hooks du module threed

const asset = require('./asset');
const audit = require('./audit');
const customEvent = require('./custom_event');
const lifecycle = require('./lifecycle');
const notification = require('./notification');

module.exports = {
  ...asset,
  ...audit,
  ...customEvent,
  ...lifecycle,
  ...notification
};

// Utilisation :
// const hooks = require('./hooks');
// hooks.assetHooks.beforeCreate(...);
// hooks.auditHooks.onAudit(...);
