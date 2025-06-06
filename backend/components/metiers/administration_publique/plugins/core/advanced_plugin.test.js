// advanced_plugin.test.js – Test JS plugin avancé
const { AdvancedPlugin } = require('./advanced_plugin');
test('AdvancedPlugin workflow', () => {
  const plugin = new AdvancedPlugin();
  expect(() => plugin.run({})).toThrow();
  plugin.activate({ user: 'admin' });
  expect(plugin.activated).toBe(true);
  const res = plugin.run({ foo: 'bar' });
  expect(res).toMatchObject({ foo: 'bar', plugin: 'advanced', status: 'ok' });
  expect(plugin.getAuditTrail().length).toBe(2);
});
