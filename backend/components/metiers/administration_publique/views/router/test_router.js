// test_router.js – Test du routeur Express pour Threed
const request = require('supertest');
const express = require('express');
const router = require('../router');

describe('Router 3D', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    app.use(router);
  });

  it('GET /3d retourne la liste des d3s', async () => {
    const res = await request(app).get('/3d');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('d3s');
    expect(res.body).toHaveProperty('total');
  });

  it('POST /3d crée un d3', async () => {
    const data = { nom: 'Test 3D', description: 'desc', type: 'objet' };
    const res = await request(app).post('/3d').send(data);
    expect([200, 201]).toContain(res.statusCode);
    expect(res.body.nom).toBe('Test 3D');
  });
});
