// test_rules.js – Tests des règles IP/CORS/API (Jest)
test('IP whitelist contient 127.0.0.1', () => {
  const whitelist = require('../rules/ip_whitelist.json');
  expect(whitelist).toContain('127.0.0.1');
});

test('CORS autorise dihya.app', () => {
  const cors = require('../rules/cors_rules.json');
  expect(cors.allowed_origins).toContain('https://dihya.app');
});
