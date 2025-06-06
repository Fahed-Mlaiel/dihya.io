// Test d'import du point d'entrée JS du sous-module utils
const utils = require('./__init__');
test('import utils entrypoint', () => {
  expect(utils).toBeDefined();
});
