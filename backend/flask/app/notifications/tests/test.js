// test.js - Tests notifications (Node.js)
const request = require('supertest');
const app = require('../../../server');
const { getJWT } = require('../../../utils/testHelpers');

describe('Notifications API', () => {
  let token;
  beforeAll(async () => {
    token = await getJWT('admin');
  });
  it('doit envoyer une notification', async () => {
    const res = await request(app)
      .post('/api/notifications')
      .set('Authorization', `Bearer ${token}`)
      .send({ message: 'Test', type: 'info' });
    expect(res.statusCode).toBe(200);
    expect(res.body.sent).toBe(true);
  });
});
