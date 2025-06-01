// main.js - Script principal de migration (REST, GraphQL, plugins, audit, RGPD, multitenancy)
// Utilisé par le système de migration Dihya

const { beforeMigrate, afterMigrate } = require('./custom/index');

async function migrate(context) {
  if (await beforeMigrate(context)) {
    // Migration principale (REST, GraphQL, plugins, audit, RGPD, multitenancy)
    // ...
    await afterMigrate(context);
  }
}

module.exports = { migrate };
