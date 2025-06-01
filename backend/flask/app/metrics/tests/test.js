// test.js - Tests métriques/monitoring (Node.js)
const request = require('supertest');
const app = require('../../../server');
const { getJWT } = require('../../../utils/testHelpers');

describe('Metrics API', () => {
  let token;
  beforeAll(async () => {
    token = await getJWT('admin');
  });
  it('doit retourner les métriques', async () => {
    const res = await request(app)
      .get('/api/metrics')
      .set('Authorization', `Bearer ${token}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('metrics');
  });
});
