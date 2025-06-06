// admin_views.test.js – Tests unitaires et conformité admin views threed (JS)
const request = require('supertest');
const express = require('express');
const adminRouter = require('./admin_views');

describe('Admin Threed', () => {
  const app = express();
  app.use(express.json());
  app.use('/admin', adminRouter);

  it('doit effectuer une action admin supportée', async () => {
    const res = await request(app)
      .post('/admin/action')
      .send({ action: 'activate', user: 'admin', details: 'test' });
    expect(res.statusCode).toBe(200);
    expect(res.body.action).toBe('activate');
    expect(res.body.user).toBe('admin');
    expect(res.body.status).toBe('success');
  });

  it('refuse une action non supportée', async () => {
    const res = await request(app)
      .post('/admin/action')
      .send({ action: 'hack', user: 'admin' });
    expect(res.statusCode).toBe(400);
  });
});
