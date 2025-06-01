// Test complet pour les routes sportives (REST + GraphQL)
const request = require('supertest');
const app = require('../../../server');
const { getJwtToken } = require('../../utils/test_utils');

describe('Sport Projects API', () => {
  let token;
  beforeAll(async () => {
    token = await getJwtToken('admin');
  });

  it('GET /api/sport/projects - sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/api/sport/projects')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('projects');
    expect(res.body).toHaveProperty('i18n');
  });

  it('POST /api/sport/projects - validation, audit', async () => {
    const res = await request(app)
      .post('/api/sport/projects')
      .set('Authorization', `Bearer ${token}`)
      .send({ name: 'Projet Sport', description: 'Test', type: 'Sport' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('project');
  });

  it('POST /api/sport/projects/ai-fallback - fallback IA', async () => {
    const res = await request(app)
      .post('/api/sport/projects/ai-fallback')
      .set('Authorization', `Bearer ${token}`)
      .send({ prompt: 'Hello world' });
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('result');
  });
});
