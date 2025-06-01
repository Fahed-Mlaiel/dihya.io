// test.js - Tests GraphQL API (Node.js)
const request = require('supertest');
const app = require('../../../server');
const { getJWT } = require('../../../utils/testHelpers');

describe('GraphQL API', () => {
  let token;
  beforeAll(async () => {
    token = await getJWT('admin');
  });
  it('doit retourner les projets IA (query)', async () => {
    const res = await request(app)
      .post('/graphql')
      .set('Authorization', `Bearer ${token}`)
      .send({ query: '{ projects { id name } }' });
    expect(res.body.data.projects).toBeInstanceOf(Array);
  });
  it('doit refuser l’accès sans JWT', async () => {
    const res = await request(app)
      .post('/graphql')
      .send({ query: '{ projects { id } }' });
    expect(res.statusCode).toBe(401);
  });
});
