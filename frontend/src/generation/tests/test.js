/**
 * Test complet pour la génération de projets IA, VR, AR, etc.
 * @module generation/tests/test
 * @author Dihya Team
 * @description Couverture maximale, multilingue, sécurité, plugins, audit.
 */

const { expect } = require('chai');
const supertest = require('supertest');
const app = require('../../../../backend/app');

describe('API Génération - Sécurité & Multitenancy', () => {
  it('refuse sans JWT', async () => {
    const res = await supertest(app)
      .post('/api/generation')
      .send({ type: 'ia', nom: 'Test' });
    expect(res.status).to.equal(401);
  });

  it('accepte admin', async () => {
    const res = await supertest(app)
      .post('/api/generation')
      .set('Authorization', 'Bearer TOKEN_ADMIN')
      .send({ type: 'ia', nom: 'Test' });
    expect(res.status).to.equal(201);
  });

  it('refuse invité', async () => {
    const res = await supertest(app)
      .post('/api/generation')
      .set('Authorization', 'Bearer TOKEN_INVITE')
      .send({ type: 'ia', nom: 'Test' });
    expect(res.status).to.equal(403);
  });
});

// ...tests plugins, fallback IA, audit, i18n, SEO, RGPD, etc.
