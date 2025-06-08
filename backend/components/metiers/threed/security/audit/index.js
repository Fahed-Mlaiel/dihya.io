// index.js – Point d'entrée principal du module audit sécurité 3D

const reportTemplates = require('./report_templates');
const policies = require('./policies');
const logExamples = require('./log_examples');
const samples = require('./samples');

module.exports = {
  reportTemplates,
  policies,
  logExamples,
  samples,
};
