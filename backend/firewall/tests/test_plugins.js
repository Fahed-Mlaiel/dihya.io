// test_plugins.js – Tests des plugins sécurité (Jest)
test('auditPlugin logge une requête', () => {
  const auditPlugin = require('../plugins/audit_plugin');
  const req = { method: 'GET', url: '/test', user: { id: 'admin' } };
  const res = {};
  let called = false;
  auditPlugin(req, res, () => { called = true; });
  expect(called).toBe(true);
});

test('rgpdPlugin anonymise l’email', () => {
  const rgpdPlugin = require('../plugins/rgpd_plugin');
  const req = { user: { id: 'u1', email: 'a@b.com' } };
  const res = {};
  rgpdPlugin(req, res, () => {});
  expect(req.user.email).toBeUndefined();
});
