// Init du sous-module models pour fixtures Threed (JS)
const fixtures = require('./fixtures');
// Exportiere alles aus fixtures und setze sample auf sample3DModel für Test-Kompatibilität
module.exports = {
  ...fixtures,
  sample: fixtures.sample3DModel
};
