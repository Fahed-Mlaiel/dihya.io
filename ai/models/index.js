// Export JS des modèles IA
module.exports = {
  model: require('./model.py'),
  config: require('./model_config.json'),
  tokenizer: require('./tokenizer.json'),
  onnx: require('./model.onnx'),
  weights: require('./model_weights.h5'),
  card: require('./model_card.md'),
};
