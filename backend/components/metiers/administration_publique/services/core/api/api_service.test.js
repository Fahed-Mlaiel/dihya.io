// api_service.test.js
// Tests unitaires ultra avancés pour ApiService (clé en main, CI/CD ready)

const ApiService = require('./api_service');

describe('ApiService', () => {
  it('doit s\'initialiser correctement', () => {
    const api = new ApiService({ mode: 'test' });
    expect(api.options).toEqual({ mode: 'test' });
    expect(api.getAuditTrail()).toEqual([]);
  });

  it('doit auditer et retourner une erreur sur requête invalide', () => {
    const api = new ApiService();
    const res = api.handleRequest(null);
    expect(res.status).toBe(400);
    expect(res.error).toBe('Invalid request');
    expect(api.getAuditTrail()[0].action).toBe('error');
  });

  it('doit traiter une requête valide et auditer', () => {
    const api = new ApiService();
    const req = { foo: 'bar' };
    const res = api.handleRequest(req);
    expect(res).toEqual({ status: 200, data: req, audited: true });
    expect(api.getAuditTrail()[1].action).toBe('request');
  });
});
