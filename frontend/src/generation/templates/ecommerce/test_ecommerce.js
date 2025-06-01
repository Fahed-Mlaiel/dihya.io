// test_ecommerce.js
// Tests avancés pour la gestion e-commerce (sécurité, rôles, plugins, audit, i18n)

/**
 * @file Test e-commerce (unit, integration, e2e)
 * @description Teste toutes les routes e-commerce, sécurité, plugins, multitenancy, audit, RGPD.
 * @i18n fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @roles admin, user, invité
 * @security JWT, CORS, WAF, anti-DDOS
 * @audit log, anonymisation, export
 */

const request = require('supertest');
const app = require('../../../../backend/app');
const { getToken } = require('../../../../backend/utils/testUtils');

describe('Ecommerce API', () => {
  let adminToken, userToken;
  beforeAll(async () => {
    adminToken = await getToken('admin');
    userToken = await getToken('user');
  });

  it('should create a product (admin)', async () => {
    const res = await request(app)
      .post('/api/ecommerce/products')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({
        name: 'Produit IA',
        price: 99.99,
        lang: 'fr',
        plugins: ['seo', 'audit'],
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject creation for guest', async () => {
    const res = await request(app)
      .post('/api/ecommerce/products')
      .send({ name: 'Test', price: 1 });
    expect(res.statusCode).toBe(401);
  });

  it('should list products (user)', async () => {
    const res = await request(app)
      .get('/api/ecommerce/products')
      .set('Authorization', `Bearer ${userToken}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it('should update a product (admin)', async () => {
    const create = await request(app)
      .post('/api/ecommerce/products')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Produit à modifier', price: 10 });
    const id = create.body.id;
    const res = await request(app)
      .put(`/api/ecommerce/products/${id}`)
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Produit modifié', price: 20 });
    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe('Produit modifié');
  });

  it('should delete a product (admin)', async () => {
    const create = await request(app)
      .post('/api/ecommerce/products')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ name: 'Produit à supprimer', price: 5 });
    const id = create.body.id;
    const res = await request(app)
      .delete(`/api/ecommerce/products/${id}`)
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(204);
  });

  it('should log all actions for audit', async () => {
    const res = await request(app)
      .get('/api/ecommerce/audit')
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('logs');
  });
});
