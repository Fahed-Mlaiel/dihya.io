// __init__.js – Initialisation des utilitaires Environnement (Node.js)
const audit = require('./audit');
const i18n = require('./i18n');
const pluginManager = require('./pluginManager');
const rbac = require('./rbac');
const samplePlugin = require('./sample_plugin');
const validators = require('./validators');
const views = require('./views');
const aiFallback = require('./ai_fallback');
const exporter = require('./exporter');
const metrics = require('./metrics');
const logger = require('./logger');

module.exports = {
  audit,
  i18n,
  pluginManager,
  rbac,
  samplePlugin,
  validators,
  views,
  aiFallback,
  exporter,
  metrics,
  logger
  // Extension : auto-discovery d'autres utils JS ici
};
