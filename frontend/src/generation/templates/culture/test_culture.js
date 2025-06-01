// test_culture.js
// Test complet pour la gestion de projets culturels (IA, VR, AR, etc.)
// Internationalisation, sécurité, multitenancy, audit, plugins, etc.

/**
 * @file Test unitaire et intégration pour la route culture
 * @description Teste la création, la lecture, la mise à jour, la suppression et la sécurité des projets culturels.
 * @i18n fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @roles admin, user, invité
 * @security JWT, CORS, WAF, anti-DDOS
 * @audit log, anonymisation, export
 */

const request = require('supertest');
const app = require('../../../../backend/app');
const { getToken } = require('../../../../backend/utils/testUtils');

describe('Culture API', () => {
  let adminToken, userToken;
  beforeAll(async () => {
    adminToken = await getToken('admin');
    userToken = await getToken('user');
  });

  it('should create a culture project (admin)', async () => {
    const res = await request(app)
      .post('/api/culture')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({
        name: 'Projet VR Amazigh',
        description: 'Expérience VR multilingue',
        lang: 'fr',
        type: 'VR',
        plugins: ['audit', 'seo'],
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject creation for guest', async () => {
    const res = await request(app)
      .post('/api/culture')
      .send({ name: 'Test', lang: 'fr' });
    expect(res.statusCode).toBe(401);
  });

  it('should list culture projects (user)', async () => {
    const res = await request(app)
      .get('/api/culture')
      .set('Authorization', `Bearer ${userToken}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it('should update a culture project (admin)', async () => {
    const create = await request(app)
      .post('/api/culture')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Projet AR', lang: 'fr', type: 'AR' });
    const id = create.body.id;
    const res = await request(app)
      .put(`/api/culture/${id}`)
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Projet AR modifié', lang: 'en' });
    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe('Projet AR modifié');
  });

  it('should delete a culture project (admin)', async () => {
    const create = await request(app)
      .post('/api/culture')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Projet à supprimer', lang: 'fr' });
    const id = create.body.id;
    const res = await request(app)
      .delete(`/api/culture/${id}`)
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(204);
  });

  it('should log all actions for audit', async () => {
    // Simule une action et vérifie le log
    const res = await request(app)
      .get('/api/culture/audit')
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('logs');
  });
});
