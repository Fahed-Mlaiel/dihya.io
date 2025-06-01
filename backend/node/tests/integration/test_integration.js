/**
 * @file test_integration.js
 * @description Test d'intégration global pour l'ensemble des APIs Dihya (sécurité, i18n, RGPD, plugins, audit, REST/GraphQL, multitenancy, etc.)
 * @author Dihya
 * @date 2025-05-25
 */

const request = require('supertest');
const app = require('../../src/app');
const { getTestToken } = require('./utils/utils');

describe('Intégration globale Dihya', () => {
  const adminToken = getTestToken('admin');
  const userToken = getTestToken('user');

  it('toutes les routes principales répondent (200, i18n, sécurité, audit)', async () => {
    const apis = [
      'loisirs', 'manufacturing', 'marketing', 'medias', 'mobile', 'mode', 'preview', 'publicite', 'recherche',
      'ressources_humaines', 'restauration', 'sante', 'science', 'securite', 'seo', 'services_personne',
      'social', 'sport', 'tourisme', 'transport'
    ];
    for (const api of apis) {
      const res = await request(app)
        .get(`/api/${api}`)
        .set('Authorization', `Bearer ${userToken}`)
        .set('Accept-Language', 'fr')
        .expect(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers).toHaveProperty('x-audit-log-id');
    }
  });

  it('GraphQL global fonctionne', async () => {
    const res = await request(app)
      .post('/graphql')
      .set('Authorization', `Bearer ${userToken}`)
      .send({ query: '{ loisirs { id nom } }' })
      .expect(200);
    expect(res.body.data).toHaveProperty('loisirs');
  });

  it('RGPD : export et anonymisation', async () => {
    const res = await request(app)
      .get('/api/loisirs/export')
      .set('Authorization', `Bearer ${userToken}`)
      .expect(200);
    expect(res.body).toHaveProperty('anonymized');
  });

  it('Plugins : activation/désactivation', async () => {
    const res = await request(app)
      .post('/api/plugins/enable')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ plugin: 'test-plugin' })
      .expect(200);
    expect(res.body).toHaveProperty('status', 'enabled');
  });
});
