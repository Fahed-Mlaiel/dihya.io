// audit.test.js – Tests unitaires JS pour audit Threed
const audit = require('./audit');
describe('Audit Threed', () => {
  it('doit retourner un score correct', () => {
    const result = audit.auditThreed({ status: 'active' });
    expect(result.score).toBe(97.0);
  });
});
