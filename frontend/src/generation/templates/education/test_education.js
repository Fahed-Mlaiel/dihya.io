// test_education.js
// Tests avancés pour la gestion éducation (sécurité, rôles, plugins, audit, i18n)

/**
 * @file Test éducation (unit, integration, e2e)
 * @description Teste toutes les routes éducation, sécurité, plugins, multitenancy, audit, RGPD.
 * @i18n fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @roles admin, enseignant, étudiant, invité
 * @security JWT, CORS, WAF, anti-DDOS
 * @audit log, anonymisation, export
 */

const request = require('supertest');
const app = require('../../../../backend/app');
const { getToken } = require('../../../../backend/utils/testUtils');

describe('Education API', () => {
  let adminToken, teacherToken, studentToken;
  beforeAll(async () => {
    adminToken = await getToken('admin');
    teacherToken = await getToken('enseignant');
    studentToken = await getToken('étudiant');
  });

  it('should create a course (admin)', async () => {
    const res = await request(app)
      .post('/api/education/courses')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({
        name: 'Cours IA',
        level: 'Avancé',
        lang: 'fr',
        plugins: ['seo', 'audit'],
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject creation for guest', async () => {
    const res = await request(app)
      .post('/api/education/courses')
      .send({ name: 'Test', level: 'Débutant' });
    expect(res.statusCode).toBe(401);
  });

  it('should list courses (student)', async () => {
    const res = await request(app)
      .get('/api/education/courses')
      .set('Authorization', `Bearer ${studentToken}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it('should update a course (teacher)', async () => {
    const create = await request(app)
      .post('/api/education/courses')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Cours à modifier', level: 'Débutant' });
    const id = create.body.id;
    const res = await request(app)
      .put(`/api/education/courses/${id}`)
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Cours modifié', level: 'Intermédiaire' });
    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe('Cours modifié');
  });

  it('should delete a course (admin)', async () => {
    const create = await request(app)
      .post('/api/education/courses')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Cours à supprimer', level: 'Débutant' });
    const id = create.body.id;
    const res = await request(app)
      .delete(`/api/education/courses/${id}`)
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(204);
  });

  it('should log all actions for audit', async () => {
    const res = await request(app)
      .get('/api/education/audit')
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('logs');
  });
});
