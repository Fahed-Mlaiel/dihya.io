// test_api.js – Tests unitaires JS pour l'API Threed
const request = require('supertest');
const express = require('express');
const api = require('../api');

describe('API Threed', () => {
  const app = express();
  app.use(api);

  it('GET /threed/:id retourne une entité 3D', async () => {
    const res = await request(app).get('/threed/1');
    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBeDefined();
    expect(res.body.status).toBe('active');
  });
});
