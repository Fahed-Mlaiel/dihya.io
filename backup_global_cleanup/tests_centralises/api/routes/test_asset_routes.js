// Test ultra avancé pour le blueprint asset_routes (Express)
const request = require('supertest');
const express = require('express');
const assetRoutes = require('../../../../blueprints/api/routes/asset_routes');

describe('assetRoutes Express', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    app.use(assetRoutes);
  });
  it('GET /assets doit répondre 200', async () => {
    const res = await request(app).get('/assets');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  it('POST /assets doit répondre 200', async () => {
    const res = await request(app).post('/assets').send({ name: 'Asset 2' });
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toMatch(/créé/);
  });
});
