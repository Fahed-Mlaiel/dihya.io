const SampleThreedPlugin = require('./samples/sample_plugin');
const AdvancedThreedPlugin = require('./core/advanced_plugin');
const pluginManager = require('./helpers/plugins_helper');

module.exports = {
  ...require('./core'),
  ...require('./helpers'),
  ...require('./samples'),
  SampleThreedPlugin,
  AdvancedThreedPlugin,
  pluginManager,
};
