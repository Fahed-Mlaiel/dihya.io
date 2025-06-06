// plugins_helper.test.js
// Tests unitaires JS pour plugins_helper
const { isValidPluginName } = require('./plugins_helper');

describe('isValidPluginName', () => {
  it('valide un nom de plugin correct', () => {
    expect(isValidPluginName('plugin-1')).toBe(true);
    expect(isValidPluginName('plugin_2')).toBe(true);
  });
  it('rejette un nom de plugin invalide', () => {
    expect(isValidPluginName('plugin!')).toBe(false);
    expect(isValidPluginName('')).toBe(false);
  });
});
