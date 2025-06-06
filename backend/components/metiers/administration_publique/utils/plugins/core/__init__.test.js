// __init__.test.js
// Test d'import du point d'entrée JS core plugins
const entry = require('./__init__.js');
describe('Import core plugins (__init__.js)', () => {
  it('should import pluginManager without error', () => {
    expect(entry).toBeDefined();
  });
});
