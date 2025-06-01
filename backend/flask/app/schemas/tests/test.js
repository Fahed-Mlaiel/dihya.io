// Tests avancés pour la validation des schémas (Node.js)
const request = require('supertest');
const app = require('../../../../app');
const { mockJwt, mockRole, mockAudit } = require('../../utils/testUtils');

describe('Schemas API', () => {
  beforeAll(() => {
    mockJwt();
    mockRole('admin');
    mockAudit();
  });

  it('should validate a schema (admin)', async () => {
    const res = await request(app)
      .post('/api/validators/validate')
      .set('Authorization', 'Bearer testtoken')
      .send({ field: 'value' });
    expect(res.statusCode).toBe(200);
    expect(res.body.msg).toBe('validated');
  });

  it('should reject invalid schema', async () => {
    const res = await request(app)
      .post('/api/validators/validate')
      .set('Authorization', 'Bearer testtoken')
      .send({});
    expect(res.statusCode).toBeGreaterThanOrEqual(400);
  });

  // ...autres tests : RGPD, plugins, audit, multilingue, e2e...
});
