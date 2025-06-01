// test.js - Tests webhooks intégrations (Node.js)
const request = require('supertest');
const app = require('../../../../server');
const { getJWT } = require('../../../../utils/testHelpers');

describe('Webhooks API', () => {
  let token;
  beforeAll(async () => {
    token = await getJWT('admin');
  });
  it('doit recevoir un webhook et répondre 200', async () => {
    const res = await request(app)
      .post('/api/integrations/webhooks')
      .set('Authorization', `Bearer ${token}`)
      .send({ event: 'test', payload: { foo: 'bar' } });
    expect(res.statusCode).toBe(200);
    expect(res.body.received).toBe(true);
  });
});
