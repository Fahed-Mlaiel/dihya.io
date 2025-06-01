// test.js - Tests templates plugins (Node.js)
const request = require('supertest');
const app = require('../../../../server');
const { getJWT } = require('../../../../utils/testHelpers');

describe('Plugin Templates API', () => {
  let token;
  beforeAll(async () => {
    token = await getJWT('admin');
  });
  it('doit retourner un template plugin', async () => {
    const res = await request(app)
      .get('/api/plugins/templates/exemple')
      .set('Authorization', `Bearer ${token}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('template');
  });
});
