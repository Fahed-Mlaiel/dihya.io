const patterns = require('./patterns_list.json');
const config = require('./patterns.config.js');

function getPattern(name) {
  return patterns.find(p => p.name === name) || null;
}

function listPatterns() {
  return patterns;
}

module.exports = {
  getPattern,
  listPatterns,
  config
};
