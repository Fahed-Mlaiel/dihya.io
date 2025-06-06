// api_views.test.js – Tests unitaires et conformité API views threed (JS)
const request = require('supertest');
const express = require('express');
const apiRouter = require('./api_views');

describe('API Threed', () => {
  const app = express();
  app.use(express.json());
  app.use('/api', apiRouter);

  it('doit rendre une vue 3D via API', async () => {
    const res = await request(app)
      .post('/api/threed/render')
      .send({ nom: 'Test', statut: 'actif', details: 'ok' });
    expect(res.statusCode).toBe(200);
    expect(res.body.nom).toBe('Test');
    expect(res.body.statut).toBe('actif');
  });
});
