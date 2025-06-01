// Tests avancés pour le scheduler (Node.js)
// Sécurité, multitenancy, plugins, audit, mocks, e2e, multilingue
const request = require('supertest');
const app = require('../../../../app');
const { mockJwt, mockRole, mockAudit } = require('../../utils/testUtils');

describe('Scheduler API', () => {
  beforeAll(() => {
    mockJwt();
    mockRole('admin');
    mockAudit();
  });

  it('should schedule a task (admin)', async () => {
    const res = await request(app)
      .post('/api/scheduler/schedule')
      .set('Authorization', 'Bearer testtoken')
      .send({ task: 'backup', time: '2025-05-25T00:00:00Z' });
    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
  });

  it('should reject unauthorized user', async () => {
    mockRole('guest');
    const res = await request(app)
      .post('/api/scheduler/schedule')
      .set('Authorization', 'Bearer testtoken')
      .send({ task: 'backup', time: '2025-05-25T00:00:00Z' });
    expect(res.statusCode).toBe(403);
  });

  // ...autres tests : plugins, audit, multilingue, e2e...
});
