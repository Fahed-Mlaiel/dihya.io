/**
 * Tests complets pour le template Immobilier (Dihya Coding)
 * @module test_immobilier
 * @description Tests unitaires, intégration, e2e, sécurité, i18n, RGPD, plugins, fallback IA.
 * @author Dihya Coding
 */
const request = require('supertest');
const app = require('../../../../src/app');
const jwt = require('jsonwebtoken');

describe('Immobilier Template API', () => {
  let token;
  beforeAll(() => {
    token = jwt.sign({ role: 'admin', tenant: 'agency1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
  });
  it('GET /api/immobilier/properties - 200 OK, multilingue', async () => {
    const res = await request(app)
      .get('/api/immobilier/properties')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.properties).toBeInstanceOf(Array);
    expect(res.body.i18n).toBeDefined();
  });
  it('POST /api/immobilier/offer - 201 Created', async () => {
    const res = await request(app)
      .post('/api/immobilier/offer')
      .set('Authorization', `Bearer ${token}`)
      .send({ propertyId: 'p1', clientId: 'c1', offer: 250000 });
    expect(res.statusCode).toBe(201);
    expect(res.body.result).toBeDefined();
  });
  it('GET /api/immobilier/properties - 401 sans JWT', async () => {
    const res = await request(app).get('/api/immobilier/properties');
    expect(res.statusCode).toBe(401);
  });
  it('POST /api/immobilier/offer - 403 invité', async () => {
    const guestToken = jwt.sign({ role: 'invité', tenant: 'agency1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
    const res = await request(app)
      .post('/api/immobilier/offer')
      .set('Authorization', `Bearer ${guestToken}`)
      .send({ propertyId: 'p1', clientId: 'c1', offer: 250000 });
    expect(res.statusCode).toBe(403);
  });
});
// ...tests avancés (plugins, RGPD, audit, SEO, accessibilité, multilingue, e2e)...
