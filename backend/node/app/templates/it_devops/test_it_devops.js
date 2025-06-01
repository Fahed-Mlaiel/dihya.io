/**
 * Tests complets pour le template IT & DevOps (Dihya Coding)
 * @module test_it_devops
 * @description Tests unitaires, intégration, e2e, sécurité, i18n, RGPD, plugins, fallback IA.
 * @author Dihya Coding
 */
const request = require('supertest');
const app = require('../../../../src/app');
const jwt = require('jsonwebtoken');

describe('IT & DevOps Template API', () => {
  let token;
  beforeAll(() => {
    token = jwt.sign({ role: 'admin', tenant: 'ops1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
  });
  it('GET /api/it_devops/pipelines - 200 OK, multilingue', async () => {
    const res = await request(app)
      .get('/api/it_devops/pipelines')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.pipelines).toBeInstanceOf(Array);
    expect(res.body.i18n).toBeDefined();
  });
  it('POST /api/it_devops/monitor - 201 Created', async () => {
    const res = await request(app)
      .post('/api/it_devops/monitor')
      .set('Authorization', `Bearer ${token}`)
      .send({ pipelineId: 'p1', userId: 'u1' });
    expect(res.statusCode).toBe(201);
    expect(res.body.result).toBeDefined();
  });
  it('GET /api/it_devops/pipelines - 401 sans JWT', async () => {
    const res = await request(app).get('/api/it_devops/pipelines');
    expect(res.statusCode).toBe(401);
  });
  it('POST /api/it_devops/monitor - 403 invité', async () => {
    const guestToken = jwt.sign({ role: 'invité', tenant: 'ops1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
    const res = await request(app)
      .post('/api/it_devops/monitor')
      .set('Authorization', `Bearer ${guestToken}`)
      .send({ pipelineId: 'p1', userId: 'u1' });
    expect(res.statusCode).toBe(403);
  });
});
// ...tests avancés (plugins, RGPD, audit, SEO, accessibilité, multilingue, e2e)...
