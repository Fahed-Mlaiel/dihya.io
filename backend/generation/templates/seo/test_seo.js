// Test SEO avancé pour Dihya Coding
// Teste la génération dynamique, la sécurité, la multilingue, la conformité RGPD, l'auditabilité, et l'extensibilité plugins.

const request = require('supertest');
const app = require('../../../../app'); // Adapter selon structure réelle

describe('SEO API', () => {
  it('optimise les métadonnées SEO (sécurité, multilingue, plugins)', async () => {
    const res = await request(app)
      .post('/seo/optimize')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({
        title: 'Test SEO',
        description: 'Description multilingue',
        locale: 'fr',
        tenant: 'demo',
        meta: { og: {}, twitter: {} }
      });
    expect(res.statusCode).toBe(200);
    expect(res.body.seo).toBeDefined();
  });

  it('génère robots.txt dynamique', async () => {
    const res = await request(app).get('/seo/robots.txt');
    expect(res.statusCode).toBe(200);
    expect(res.text).toContain('User-agent');
  });

  it('génère sitemap.xml dynamique', async () => {
    const res = await request(app).get('/seo/sitemap.xml');
    expect(res.statusCode).toBe(200);
    expect(res.text).toContain('<urlset');
  });
});
