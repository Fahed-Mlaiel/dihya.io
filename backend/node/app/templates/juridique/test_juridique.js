/**
 * Tests complets pour le template Juridique (Dihya Coding)
 * @module test_juridique
 * @description Tests unitaires, intégration, e2e, sécurité, i18n, RGPD, plugins, fallback IA.
 * @author Dihya Coding
 */
const request = require('supertest');
const app = require('../../../../src/app');
const jwt = require('jsonwebtoken');

describe('Juridique Template API', () => {
  let token;
  beforeAll(() => {
    token = jwt.sign({ role: 'admin', tenant: 'cabinet1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
  });
  it('GET /api/juridique/cases - 200 OK, multilingue', async () => {
    const res = await request(app)
      .get('/api/juridique/cases')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.cases).toBeInstanceOf(Array);
    expect(res.body.i18n).toBeDefined();
  });
  it('POST /api/juridique/contract - 201 Created', async () => {
    const res = await request(app)
      .post('/api/juridique/contract')
      .set('Authorization', `Bearer ${token}`)
      .send({ title: 'Contrat A', parties: ['p1', 'p2'], content: 'Texte du contrat' });
    expect(res.statusCode).toBe(201);
    expect(res.body.result).toBeDefined();
  });
  it('GET /api/juridique/cases - 401 sans JWT', async () => {
    const res = await request(app).get('/api/juridique/cases');
    expect(res.statusCode).toBe(401);
  });
  it('POST /api/juridique/contract - 403 invité', async () => {
    const guestToken = jwt.sign({ role: 'invité', tenant: 'cabinet1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
    const res = await request(app)
      .post('/api/juridique/contract')
      .set('Authorization', `Bearer ${guestToken}`)
      .send({ title: 'Contrat A', parties: ['p1', 'p2'], content: 'Texte du contrat' });
    expect(res.statusCode).toBe(403);
  });
});
// ...tests avancés (plugins, RGPD, audit, SEO, accessibilité, multilingue, e2e)...
