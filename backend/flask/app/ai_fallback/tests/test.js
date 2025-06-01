// test.js - Tests unitaires et intégration fallback IA (Node.js)
const request = require('supertest');
const app = require('../../../server');
const { getJWT } = require('../../../utils/testHelpers');

describe('Fallback IA API', () => {
  let token;
  beforeAll(async () => {
    token = await getJWT('admin');
  });
  it('doit fallback sur LLaMA si Mixtral indisponible', async () => {
    const res = await request(app)
      .post('/api/ai/fallback')
      .set('Authorization', `Bearer ${token}`)
      .send({ prompt: 'test', provider: 'mixtral' });
    expect(res.body.provider).toMatch(/llama|mistral/i);
    expect(res.body.fallback).toBe(true);
  });
});
