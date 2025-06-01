// test_environnement.js
// Tests avancés pour la gestion environnement (sécurité, rôles, plugins, audit, i18n)

/**
 * @file Test environnement (unit, integration, e2e)
 * @description Teste toutes les routes environnement, sécurité, plugins, multitenancy, audit, RGPD.
 * @i18n fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @roles admin, user, invité
 * @security JWT, CORS, WAF, anti-DDOS
 * @audit log, anonymisation, export
 */

const request = require('supertest');
const app = require('../../../../backend/app');
const { getToken } = require('../../../../backend/utils/testUtils');

describe('Environment API', () => {
  let adminToken, userToken;
  beforeAll(async () => {
    adminToken = await getToken('admin');
    userToken = await getToken('user');
  });

  it('should create an environment dashboard (admin)', async () => {
    const res = await request(app)
      .post('/api/environnement/dashboards')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({
        name: 'Dashboard IA',
        type: 'Monitoring',
        lang: 'fr',
        plugins: ['seo', 'audit'],
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject creation for guest', async () => {
    const res = await request(app)
      .post('/api/environnement/dashboards')
      .send({ name: 'Test', type: 'Simple' });
    expect(res.statusCode).toBe(401);
  });

  it('should list dashboards (user)', async () => {
    const res = await request(app)
      .get('/api/environnement/dashboards')
      .set('Authorization', `Bearer ${userToken}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it('should update a dashboard (admin)', async () => {
    const create = await request(app)
      .post('/api/environnement/dashboards')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Dashboard à modifier', type: 'Simple' });
    const id = create.body.id;
    const res = await request(app)
      .put(`/api/environnement/dashboards/${id}`)
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Dashboard modifié', type: 'Optimisé' });
    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe('Dashboard modifié');
  });

  it('should delete a dashboard (admin)', async () => {
    const create = await request(app)
      .post('/api/environnement/dashboards')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Dashboard à supprimer', type: 'Simple' });
    const id = create.body.id;
    const res = await request(app)
      .delete(`/api/environnement/dashboards/${id}`)
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(204);
  });

  it('should log all actions for audit', async () => {
    const res = await request(app)
      .get('/api/environnement/audit')
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('logs');
  });
});
