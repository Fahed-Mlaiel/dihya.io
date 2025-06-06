// index.js – Point d'entrée central JS pour tous les utilitaires du module threed
module.exports = {
  ...require('./ai/ai_fallback'),
  ...require('./audit/audit'),
  ...require('./exporter/exporter'),
  ...require('./helpers/utils_helper'),
  ...require('./i18n/i18n'),
  ...require('./logger/logger'),
  ...require('./metrics/metrics'),
  ...require('./plugins/pluginManager'),
  ...require('./plugins/sample_plugin'),
  ...require('./rbac/rbac'),
  ...require('./validators/validators'),
  ...require('./views/views')
};
