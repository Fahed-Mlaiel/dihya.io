// __init__.js – Initialisation JS exporter pour CI/CD, audit, conformité
module.exports = {
  ...require('./core'),
  ...require('./helpers'),
  ...require('./fallback'),
  ...require('./samples'),
};
