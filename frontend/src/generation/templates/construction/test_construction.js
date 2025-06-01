// test_construction.js
// Test complet pour le template construction (sécurité, RGPD, plugins, multilingue, audit, etc.)
const { generateConstructionProject } = require('./template');
const { mockRequest, mockResponse, mockNext } = require('../../../../utils/testUtils');
const { expect } = require('chai');

describe('Construction Template', () => {
  it('génère un projet construction sécurisé, multilingue, RGPD', async () => {
    const req = mockRequest({
      body: {
        name: 'Construction IA',
        lang: 'es',
        tenant: 'construct',
        userRole: 'admin',
        features: ['RGPD', 'AI'],
      },
      user: { id: '6', role: 'admin', tenant: 'construct' },
    });
    const res = mockResponse();
    await generateConstructionProject(req, res, mockNext);
    expect(res.status.calledWith(201)).to.be.true;
    expect(res.json.called).to.be.true;
    const data = res.json.firstCall.args[0];
    expect(data.project.name).to.equal('Construction IA');
    expect(data.project.security.rgpd).to.be.true;
    expect(data.project.plugins.length).to.be.greaterThan(0);
    expect(data.project.i18n).to.have.property('es');
  });
});
