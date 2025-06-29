// Export JS des providers IA
module.exports = {
  openai: require('./openai_provider.py'),
  huggingface: require('./huggingface_provider.py'),
  azure: require('./azure_provider.py'),
  config: require('./provider_config.json'),
};
