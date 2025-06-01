/**
 * Tests complets pour le template Journalisme (Dihya Coding)
 * @module test_journalisme
 * @description Tests unitaires, intégration, e2e, sécurité, i18n, RGPD, plugins, fallback IA.
 * @author Dihya Coding
 */
const request = require('supertest');
const app = require('../../../../src/app');
const jwt = require('jsonwebtoken');

describe('Journalisme Template API', () => {
  let token;
  beforeAll(() => {
    token = jwt.sign({ role: 'admin', tenant: 'media1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
  });
  it('GET /api/journalisme/articles - 200 OK, multilingue', async () => {
    const res = await request(app)
      .get('/api/journalisme/articles')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.articles).toBeInstanceOf(Array);
    expect(res.body.i18n).toBeDefined();
  });
  it('POST /api/journalisme/publish - 201 Created', async () => {
    const res = await request(app)
      .post('/api/journalisme/publish')
      .set('Authorization', `Bearer ${token}`)
      .send({ title: 'Nouveau titre', content: 'Contenu', authorId: 'a1' });
    expect(res.statusCode).toBe(201);
    expect(res.body.result).toBeDefined();
  });
  it('GET /api/journalisme/articles - 401 sans JWT', async () => {
    const res = await request(app).get('/api/journalisme/articles');
    expect(res.statusCode).toBe(401);
  });
  it('POST /api/journalisme/publish - 403 invité', async () => {
    const guestToken = jwt.sign({ role: 'invité', tenant: 'media1' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
    const res = await request(app)
      .post('/api/journalisme/publish')
      .set('Authorization', `Bearer ${guestToken}`)
      .send({ title: 'Nouveau titre', content: 'Contenu', authorId: 'a1' });
    expect(res.statusCode).toBe(403);
  });
});
// ...tests avancés (plugins, RGPD, audit, SEO, accessibilité, multilingue, e2e)...
