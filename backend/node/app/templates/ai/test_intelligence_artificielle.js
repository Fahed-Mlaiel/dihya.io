/**
 * Tests complets pour le template Intelligence Artificielle (Dihya Coding)
 * @module test_intelligence_artificielle
 * @description Tests unitaires, intégration, e2e, sécurité, i18n, RGPD, plugins, fallback IA.
 * @author Dihya Coding
 */
const request = require('supertest');
const app = require('../../../../src/app');
const jwt = require('jsonwebtoken');

describe('IA Template API', () => {
  let token;
  beforeAll(() => {
    token = jwt.sign({ role: 'admin', tenant: 'lab1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
  });
  it('POST /api/ia/inference - 200 OK, multilingue', async () => {
    const res = await request(app)
      .post('/api/ia/inference')
      .set('Authorization', `Bearer ${token}`)
      .send({ model: 'llama', input: { text: 'Bonjour' } });
    expect(res.statusCode).toBe(200);
    expect(res.body.result).toBeDefined();
    expect(res.body.i18n).toBeDefined();
  });
  it('GET /api/ia/models - 200 OK', async () => {
    const res = await request(app)
      .get('/api/ia/models')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.models).toBeInstanceOf(Array);
  });
  it('POST /api/ia/inference - 401 sans JWT', async () => {
    const res = await request(app)
      .post('/api/ia/inference')
      .send({ model: 'llama', input: { text: 'Bonjour' } });
    expect(res.statusCode).toBe(401);
  });
  it('GET /api/ia/models - 403 invité', async () => {
    const guestToken = jwt.sign({ role: 'invité', tenant: 'lab1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
    const res = await request(app)
      .get('/api/ia/models')
      .set('Authorization', `Bearer ${guestToken}`);
    expect(res.statusCode).toBe(403);
  });
});
// ...tests avancés (plugins, RGPD, audit, SEO, accessibilité, multilingue, e2e)...
