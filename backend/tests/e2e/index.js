// E2E tests pour backend Dihya (routes, plugins, sécurité, i18n, audit)
const request = require('supertest');
const app = require('../../app');

describe('E2E Backend Dihya', () => {
  it('Valide la création de projet IA', async () => {
    const res = await request(app)
      .post('/validators/project')
      .send({
        name: 'Projet IA',
        description: 'Projet IA avancé',
        type: 'IA',
        owner_email: 'test@dihya.org',
      })
      .set('Authorization', 'Bearer testtoken');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('ok');
  });

  it('Test synthèse vocale', async () => {
    const res = await request(app)
      .post('/voice/synthesize')
      .send({ text: 'Bonjour', lang: 'fr' })
      .set('Authorization', 'Bearer testtoken');
    expect(res.statusCode).toBe(200);
    expect(res.body.audio).toBeDefined();
  });
});
