// Tests unitaires avancés pour la plateforme Dihya (Node.js/Jest)
// Sécurité, i18n, plugins, RGPD, audit, SEO, fallback IA, multitenancy, etc.
const request = require('supertest');
const app = require('../../../backend/app');

describe('API Dihya - Tests avancés', () => {
  it('GET /api/arts/ doit retourner la liste des projets arts', async () => {
    const res = await request(app).get('/api/arts/?lang=fr');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('projects');
    expect(Array.isArray(res.body.projects)).toBe(true);
  });

  it('POST /api/arts/ crée un projet avec JWT', async () => {
    const res = await request(app)
      .post('/api/arts/')
      .set('Authorization', 'Bearer test.jwt.token')
      .send({ name: 'Projet IA', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body.name).toBe('Projet IA');
  });

  it('POST /api/arts/graphql supporte GraphQL', async () => {
    const res = await request(app)
      .post('/api/arts/graphql')
      .send({ query: '{ arts { id name } }' });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('arts');
  });

  it('GET /api/arts/?lang=ar supporte i18n', async () => {
    const res = await request(app).get('/api/arts/?lang=ar');
    expect(res.statusCode).toBe(200);
    expect(res.body.lang).toBe('ar');
  });

  it('GET /api/arts/?plugin=seo supporte plugins dynamiques', async () => {
    const res = await request(app).get('/api/arts/?plugin=seo');
    expect(res.statusCode).toBe(200);
    expect(res.body.plugin).toBe('seo');
  });

  it('GET /api/arts/export RGPD export', async () => {
    const res = await request(app)
      .get('/api/arts/export')
      .set('Authorization', 'Bearer test.jwt.token');
    expect(res.statusCode).toBe(200);
    expect(res.body.export.format).toBe('csv');
  });
});
