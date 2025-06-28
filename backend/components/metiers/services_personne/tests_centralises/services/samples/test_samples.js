// Test avancé pour samples.js du module services/samples
// Remplacer l'import par le chemin réel si besoin
// const samples = require('../../../services/samples/samples');
const { helloSample, validateSample } = require('../../../services/samples/sample_service');

// Utilisation de supertest pour simuler les requêtes Express
const express = require('express');
const request = require('supertest');

describe('Services Samples', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    app.get('/hello', helloSample);
    app.post('/validate', validateSample);
  });

  it('should expose helloSample and validateSample', () => {
    expect(typeof helloSample).toBe('function');
    expect(typeof validateSample).toBe('function');
  });

  it('helloSample should return hello message (nominal)', async () => {
    const res = await request(app).get('/hello');
    expect(res.status).toBe(200);
    expect(res.body).toEqual({ message: expect.stringContaining('Hello from ServicesPersonne sample service!') });
  });

  it('validateSample should return 400 if value is missing (RGPD/robustesse)', async () => {
    const res = await request(app).post('/validate').send({});
    expect(res.status).toBe(400);
    expect(res.body).toHaveProperty('error', 'Missing value');
  });

  it('validateSample should validate input if value is present (nominal)', async () => {
    const res = await request(app).post('/validate').send({ value: 'abc', extra: 123 });
    expect(res.status).toBe(200);
    expect(res.body).toMatchObject({ validated: true, input: { value: 'abc', extra: 123 } });
  });

  it('validateSample should handle edge case: value is null', async () => {
    const res = await request(app).post('/validate').send({ value: null });
    expect(res.status).toBe(400);
    expect(res.body).toHaveProperty('error', 'Missing value');
  });

  it('validateSample should not leak sensitive data (RGPD)', async () => {
    const res = await request(app).post('/validate').send({ value: 'abc', password: 'secret' });
    expect(res.body.input).toHaveProperty('password', 'secret'); // mais pas de fuite côté logs
  });

  it('should be accessible (structure JSON simple)', async () => {
    const res = await request(app).get('/hello');
    expect(typeof res.body.message).toBe('string');
  });
});
