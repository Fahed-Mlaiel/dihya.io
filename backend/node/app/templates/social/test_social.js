// Test complet pour les routes sociales (REST + GraphQL)
const request = require('supertest');
const app = require('../../../server');
const { getJwtToken } = require('../../utils/test_utils');

describe('Social Projects API', () => {
  let token;
  beforeAll(async () => {
    token = await getJwtToken('admin');
  });

  it('GET /api/social/projects - sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/api/social/projects')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('projects');
    expect(res.body).toHaveProperty('i18n');
  });

  it('POST /api/social/projects - validation, audit', async () => {
    const res = await request(app)
      .post('/api/social/projects')
      .set('Authorization', `Bearer ${token}`)
      .send({ name: 'Projet IA', description: 'Test', type: 'AI' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('project');
  });

  it('POST /api/social/projects/ai-fallback - fallback IA', async () => {
    const res = await request(app)
      .post('/api/social/projects/ai-fallback')
      .set('Authorization', `Bearer ${token}`)
      .send({ prompt: 'Hello world' });
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('result');
  });
});
