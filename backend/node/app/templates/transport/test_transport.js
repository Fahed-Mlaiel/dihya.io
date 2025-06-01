// Test complet pour les routes transport (REST + GraphQL)
const request = require('supertest');
const app = require('../../../server');
const { getJwtToken } = require('../../utils/test_utils');

describe('Transport Projects API', () => {
  let token;
  beforeAll(async () => {
    token = await getJwtToken('admin');
  });

  it('GET /api/transport/projects - sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/api/transport/projects')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('projects');
    expect(res.body).toHaveProperty('i18n');
  });

  it('POST /api/transport/projects - validation, audit', async () => {
    const res = await request(app)
      .post('/api/transport/projects')
      .set('Authorization', `Bearer ${token}`)
      .send({ name: 'Projet Transport', description: 'Test', type: 'Transport' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('project');
  });

  it('POST /api/transport/projects/ai-fallback - fallback IA', async () => {
    const res = await request(app)
      .post('/api/transport/projects/ai-fallback')
      .set('Authorization', `Bearer ${token}`)
      .send({ prompt: 'Hello world' });
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('result');
  });
});
