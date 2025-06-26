// test_sample_audit.js – Test ultra avancé des samples audit API Juridique (centralisé)

const { sampleAuditLogAction } = require('../../../api/samples/audit');

describe('Samples Audit API Juridique', () => {
  it('doit logger une action API avec tous les contextes', () => {
    const action = 'create';
    const user = { id: 1, name: 'Alice' };
    const data = { name: 'UltraDossier', status: 'active' };
    const result = sampleAuditLogAction(action, user, data);
    expect(result.action).toBe(action);
    expect(result.user).toEqual(user);
    expect(result.data).toEqual(data);
    expect(result.status).toBe('logged');
    expect(result.timestamp).toBeDefined();
  });
});
