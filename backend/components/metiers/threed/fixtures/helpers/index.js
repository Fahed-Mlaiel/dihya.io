// index.js – Point d’entrée principal JS (fusionne tous les helpers)
module.exports = {
  ...require('./helpers'),
  ...require('./validators'),
};
