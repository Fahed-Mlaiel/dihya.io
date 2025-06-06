const fs = require('fs');
module.exports.discover = () => {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
};
