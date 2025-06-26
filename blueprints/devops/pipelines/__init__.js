const fs = require('fs');
// Initialisation des pipelines CI/CD (Node.js)
const ciCd = require('./ci_cd');
const pipelines = { ciCd };
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js' && file !== 'ci_cd.js') {
    const name = file.replace('.js', '');
    pipelines[name] = require('./' + file);
  }
});

module.exports = pipelines;
