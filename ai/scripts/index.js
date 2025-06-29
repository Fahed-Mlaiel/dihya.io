// Export JS des scripts IA
module.exports = {
  generate: require('./generate_ai_project.py'),
  train: require('./train_model.py'),
  infer: require('./infer.py'),
  preprocess: require('./preprocess.py'),
};
