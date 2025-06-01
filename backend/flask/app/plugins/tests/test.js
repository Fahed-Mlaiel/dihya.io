// test.js - Tests plugins (Node.js)
const request = require('supertest');
const app = require('../../../server');
const { getJWT } = require('../../../utils/testHelpers');

describe('Plugins API', () => {
  let token;
  beforeAll(async () => {
    token = await getJWT('admin');
  });
  it('doit activer le plugin exemple', async () => {
    const res = await request(app)
      .get('/api/plugins/exemple')
      .set('Authorization', `Bearer ${token}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toMatch(/exemple/i);
  });
});
