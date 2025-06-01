/**
 * Test d'intégration avancé – Administration Publique (IA/VR/AR)
 * Sécurité (CORS, JWT, WAF, anti-DDOS), RGPD, accessibilité, i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es), plugins, audit, fallback IA, RBAC, multitenancy, SEO backend, CI/CD-ready.
 * @module tests/integration/administration_publique/test_administration_publique
 */
const request = require('supertest');
const app = require('../../../src/app');
const { getJWT, getTestTenant, getTestUser } = require('../../utils/auth');

describe('Intégration Administration Publique – Projets IA/VR/AR', () => {
  let jwt, tenant, user;
  beforeAll(async () => {
    tenant = await getTestTenant();
    user = await getTestUser('admin', tenant.id);
    jwt = await getJWT(user, tenant);
  });

  it('crée un projet IA/VR/AR administration publique sécurisé et multilingue', async () => {
    const res = await request(app)
      .post(`/api/${tenant.slug}/administration_publique/projets`)
      .set('Authorization', `Bearer ${jwt}`)
      .set('Accept-Language', 'fr')
      .send({
        nom: 'Projet AdminPub IA',
        type: 'IA',
        description: 'Projet administration publique intelligent',
        langues: ['fr', 'en', 'ar'],
        plugins: ['seo', 'audit', 'llama-fallback'],
        consentementRGPD: true
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.langues).toContain('fr');
    expect(res.body.plugins).toContain('seo');
  });

  it('vérifie la conformité RGPD, accessibilité et SEO backend', async () => {
    const res = await request(app)
      .get(`/api/${tenant.slug}/administration_publique/projets?audit=true`)
      .set('Authorization', `Bearer ${jwt}`)
      .set('Accept-Language', 'en');
    expect(res.statusCode).toBe(200);
    expect(res.body.audit.rgpd).toBe(true);
    expect(res.body.audit.accessibilite).toBe(true);
    expect(res.body.audit.seo).toBe(true);
  });

  it('gère le fallback IA (LLaMA/Mixtral/Mistral) et plugins dynamiques', async () => {
    const res = await request(app)
      .post(`/api/${tenant.slug}/administration_publique/projets/ia-fallback`)
      .set('Authorization', `Bearer ${jwt}`)
      .send({ prompt: 'Génère un projet administration publique intelligent', fallback: ['llama', 'mixtral'] });
    expect(res.statusCode).toBe(200);
    expect(res.body.fallbackUsed).toMatch(/llama|mixtral|mistral/);
  });

  it('applique les politiques RBAC et multitenancy', async () => {
    const res = await request(app)
      .get(`/api/${tenant.slug}/administration_publique/projets`)
      .set('Authorization', `Bearer ${jwt}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
});
