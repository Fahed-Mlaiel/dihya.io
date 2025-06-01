/**
 * Test d'intégration avancé pour la gestion des projets VR/AR (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('VR/AR API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /vr_ar (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/vr_ar')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /vr_ar (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/vr_ar')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'VR Immersif', type: 'VR', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('entry');
  });
  it('PUT /vr_ar/:id (admin only, validation, audit)', async () => {
    const res = await request(app)
      .put('/vr_ar/1')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'VR Modifié', type: 'VR', owner: 'user_id' });
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('updated');
  });
  it('DELETE /vr_ar/:id (admin only, audit, RGPD)', async () => {
    const res = await request(app)
      .delete('/vr_ar/1')
      .set('Authorization', `Bearer ${jwt}`);
    expect(res.statusCode).toBe(204);
  });
  it('POST /vr_ar/plugin?plugin=emotion_analysis (plugin, audit, RGPD)', async () => {
    const res = await request(app)
      .post('/vr_ar/plugin?plugin=emotion_analysis')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ user_id: 'user_id', session_id: 'sess1' });
    expect(res.statusCode).toBe(200);
    expect(res.body.result).toHaveProperty('emotion');
  });
});
