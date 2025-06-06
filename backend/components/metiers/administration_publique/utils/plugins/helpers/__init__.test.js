// __init__.test.js
// Test d'import du point d'entrée JS helpers plugins
const entry = require('./__init__.js');
describe('Import helpers plugins (__init__.js)', () => {
  it('should import plugins_helper without error', () => {
    expect(entry).toBeDefined();
  });
});
