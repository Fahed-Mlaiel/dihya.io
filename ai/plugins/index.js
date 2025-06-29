// Export JS des plugins IA
module.exports = {
  analytics: require('./analytics_plugin.py'),
  cms: require('./cms_plugin.py'),
  stripe: require('./stripe_plugin.py'),
  config: require('./plugin_config.json'),
};
