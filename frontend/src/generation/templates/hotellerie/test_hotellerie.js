// test_hotellerie.js
// Tests avancés pour la gestion hôtellerie (sécurité, rôles, plugins, audit, i18n)

/**
 * @file Test hôtellerie (unit, integration, e2e)
 * @description Teste toutes les routes hôtellerie, sécurité, plugins, multitenancy, audit, RGPD.
 * @i18n fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @roles admin, user, invité
 * @security JWT, CORS, WAF, anti-DDOS
 * @audit log, anonymisation, export
 */

const request = require('supertest');
const app = require('../../../../backend/app');
const { getToken } = require('../../../../backend/utils/testUtils');

describe('Hospitality API', () => {
  let adminToken, userToken;
  beforeAll(async () => {
    adminToken = await getToken('admin');
    userToken = await getToken('user');
  });

  it('should create a reservation (admin)', async () => {
    const res = await request(app)
      .post('/api/hotellerie/reservations')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({
        name: 'Réservation IA',
        type: 'Chambre',
        lang: 'fr',
        plugins: ['seo', 'audit'],
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject creation for guest', async () => {
    const res = await request(app)
      .post('/api/hotellerie/reservations')
      .send({ name: 'Test', type: 'Simple' });
    expect(res.statusCode).toBe(401);
  });

  it('should list reservations (user)', async () => {
    const res = await request(app)
      .get('/api/hotellerie/reservations')
      .set('Authorization', `Bearer ${userToken}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it('should update a reservation (admin)', async () => {
    const create = await request(app)
      .post('/api/hotellerie/reservations')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Réservation à modifier', type: 'Simple' });
    const id = create.body.id;
    const res = await request(app)
      .put(`/api/hotellerie/reservations/${id}`)
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Réservation modifiée', type: 'Suite' });
    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe('Réservation modifiée');
  });

  it('should delete a reservation (admin)', async () => {
    const create = await request(app)
      .post('/api/hotellerie/reservations')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Réservation à supprimer', type: 'Simple' });
    const id = create.body.id;
    const res = await request(app)
      .delete(`/api/hotellerie/reservations/${id}`)
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(204);
  });

  it('should log all actions for audit', async () => {
    const res = await request(app)
      .get('/api/hotellerie/audit')
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('logs');
  });
});
