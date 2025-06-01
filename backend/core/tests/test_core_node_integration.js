// Test d’intégration Node.js/Express pour le core Dihya (RBAC, logs, plugins, i18n, audit)
const express = require('express');
const request = require('supertest');
const core = require('../index');

describe('Core Node.js/Express Integration', () => {
  let app;
  beforeEach(() => {
    app = express();
    app.use(core.securityHeaders);
    app.get('/api/secure', core.rbac('admin'), (req, res) => {
      res.json({ data: 'secret', lang: core.getLang(req) });
    });
  });

  it('autorise l’accès admin', async () => {
    const res = await request(app)
      .get('/api/secure')
      .set('X-Dihya-Role', 'admin')
      .set('X-Dihya-Lang', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toBe('secret');
    expect(res.body.lang).toBe('fr');
  });

  it('refuse l’accès guest', async () => {
    const res = await request(app)
      .get('/api/secure')
      .set('X-Dihya-Role', 'guest')
      .set('X-Dihya-Lang', 'en');
    expect(res.statusCode).toBe(403);
    expect(res.body.error).toBe('Access denied');
  });
});
