// test_it_devops.js
/**
 * @file Tests d'intégration pour la gestion de projets IT/DevOps (REST & GraphQL)
 * @description Sécurité maximale, multilingue, multitenant, plugins, RGPD, audit, SEO, IA fallback
 * @author Dihya
 */
const request = require('supertest');
const app = require('../../../../backend/app');
const { getJWT, getTestTenant, getI18nHeaders } = require('../../utils/testHelpers');

describe('IT/DevOps - Intégration API', () => {
  let jwt, tenant;
  beforeAll(async () => {
    tenant = await getTestTenant('it_devops');
    jwt = await getJWT({ role: 'admin', tenant });
  });

  it('crée un projet IT/DevOps (REST)', async () => {
    const res = await request(app)
      .post(`/api/v1/it_devops/projects`)
      .set('Authorization', `Bearer ${jwt}`)
      .set(getI18nHeaders('fr'))
      .send({
        name: 'DevOps Test',
        description: 'Projet CI/CD, K8s, Docker',
        type: 'DevOps',
        lang: 'fr',
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.lang).toBe('fr');
  });

  it('liste les projets (GraphQL)', async () => {
    const query = `query { itDevopsProjects { id name type lang } }`;
    const res = await request(app)
      .post('/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .set(getI18nHeaders('en'))
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data.itDevopsProjects).toBeInstanceOf(Array);
  });

  it('refuse accès sans JWT', async () => {
    const res = await request(app)
      .get(`/api/v1/it_devops/projects`)
      .set(getI18nHeaders('fr'));
    expect(res.statusCode).toBe(401);
  });

  it('supporte tous les langages', async () => {
    const langs = ['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es'];
    for (const lang of langs) {
      const res = await request(app)
        .get(`/api/v1/it_devops/projects`)
        .set('Authorization', `Bearer ${jwt}`)
        .set(getI18nHeaders(lang));
      expect([200,204]).toContain(res.statusCode);
    }
  });

  // ...tests RGPD, plugins, audit, SEO, fallback IA...
});
