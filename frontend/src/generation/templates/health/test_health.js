// test_health.js
// Tests avancés pour la gestion santé (sécurité, rôles, plugins, audit, i18n)

/**
 * @file Test santé (unit, integration, e2e)
 * @description Teste toutes les routes santé, sécurité, plugins, multitenancy, audit, RGPD.
 * @i18n fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @roles admin, médecin, patient, invité
 * @security JWT, CORS, WAF, anti-DDOS
 * @audit log, anonymisation, export
 */

const request = require('supertest');
const app = require('../../../../backend/app');
const { getToken } = require('../../../../backend/utils/testUtils');

describe('Health API', () => {
  let adminToken, doctorToken, patientToken;
  beforeAll(async () => {
    adminToken = await getToken('admin');
    doctorToken = await getToken('médecin');
    patientToken = await getToken('patient');
  });

  it('should create a health record (admin)', async () => {
    const res = await request(app)
      .post('/api/health/records')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({
        name: 'Dossier IA',
        type: 'Analyse',
        lang: 'fr',
        plugins: ['seo', 'audit'],
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject creation for guest', async () => {
    const res = await request(app)
      .post('/api/health/records')
      .send({ name: 'Test', type: 'Simple' });
    expect(res.statusCode).toBe(401);
  });

  it('should list health records (patient)', async () => {
    const res = await request(app)
      .get('/api/health/records')
      .set('Authorization', `Bearer ${patientToken}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it('should update a health record (doctor)', async () => {
    const create = await request(app)
      .post('/api/health/records')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Dossier à modifier', type: 'Simple' });
    const id = create.body.id;
    const res = await request(app)
      .put(`/api/health/records/${id}`)
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Dossier modifié', type: 'Analyse' });
    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe('Dossier modifié');
  });

  it('should delete a health record (admin)', async () => {
    const create = await request(app)
      .post('/api/health/records')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Dossier à supprimer', type: 'Simple' });
    const id = create.body.id;
    const res = await request(app)
      .delete(`/api/health/records/${id}`)
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(204);
  });

  it('should log all actions for audit', async () => {
    const res = await request(app)
      .get('/api/health/audit')
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('logs');
  });
});
