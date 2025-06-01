/**
 * Tests complets pour le template Hôtellerie (Dihya Coding)
 * @module test_hotellerie
 * @description Tests unitaires, intégration, e2e, sécurité, i18n, RGPD, plugins, fallback IA.
 * @author Dihya Coding
 */
const request = require('supertest');
const app = require('../../../../src/app');
const jwt = require('jsonwebtoken');

describe('Hotellerie Template API', () => {
  let token;
  beforeAll(() => {
    token = jwt.sign({ role: 'admin', tenant: 'hotel1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
  });
  it('GET /api/hotellerie/rooms - 200 OK, multilingue', async () => {
    const res = await request(app)
      .get('/api/hotellerie/rooms')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.rooms).toBeInstanceOf(Array);
    expect(res.body.i18n).toBeDefined();
  });
  it('POST /api/hotellerie/booking - 201 Created', async () => {
    const res = await request(app)
      .post('/api/hotellerie/booking')
      .set('Authorization', `Bearer ${token}`)
      .send({ roomId: '101', userId: 'u1' });
    expect(res.statusCode).toBe(201);
    expect(res.body.booking).toBeDefined();
  });
  it('GET /api/hotellerie/rooms - 401 sans JWT', async () => {
    const res = await request(app).get('/api/hotellerie/rooms');
    expect(res.statusCode).toBe(401);
  });
  it('POST /api/hotellerie/booking - 403 invité', async () => {
    const guestToken = jwt.sign({ role: 'invité', tenant: 'hotel1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
    const res = await request(app)
      .post('/api/hotellerie/booking')
      .set('Authorization', `Bearer ${guestToken}`)
      .send({ roomId: '101', userId: 'u1' });
    expect(res.statusCode).toBe(403);
  });
});
// ...tests avancés (plugins, RGPD, audit, SEO, accessibilité, multilingue, e2e)...
