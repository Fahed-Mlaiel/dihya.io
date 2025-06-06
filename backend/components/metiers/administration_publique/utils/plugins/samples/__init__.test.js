// __init__.test.js
// Test d'import du point d'entrée JS samples plugins
const entry = require('./__init__.js');
describe('Import samples plugins (__init__.js)', () => {
  it('should import sample and test without error', () => {
    expect(entry.sample).toBeDefined();
    expect(entry.test).toBeDefined();
  });
});
