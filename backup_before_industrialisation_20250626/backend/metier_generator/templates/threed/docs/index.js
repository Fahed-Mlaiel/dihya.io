// Index clé en main pour toute la documentation du module threed

const api = require('./api');
const architecture = require('./architecture');
const changelog = require('./changelog');
const faq = require('./faq');
const integration = require('./integration');
const security = require('./security');
const tutorials = require('./tutorials');

module.exports = {
  ...api,
  ...architecture,
  ...changelog,
  ...faq,
  ...integration,
  ...security,
  ...tutorials
};

// Utilisation :
// const docs = require('./docs');
// docs.openapi
// docs.architectureDoc
// docs.changelog
// docs.faq
// docs.integrationGuide
// docs.securityDoc
// docs.helloWorldTutorial
