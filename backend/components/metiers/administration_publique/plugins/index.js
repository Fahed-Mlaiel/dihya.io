const SampleThreedPlugin = require('./sample_plugin');
const AdvancedThreedPlugin = require('./advanced_plugin');
const pluginManager = require('./plugins');

module.exports = {
  ...require('./core'),
  ...require('./helpers'),
  ...require('./samples'),
  SampleThreedPlugin,
  AdvancedThreedPlugin,
  pluginManager,
};
