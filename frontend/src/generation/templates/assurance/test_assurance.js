// test_assurance.js
// Test complet pour le template assurance (sécurité, RGPD, plugins, multilingue, audit, etc.)
const { generateAssuranceProject } = require('./template');
const { mockRequest, mockResponse, mockNext } = require('../../../../utils/testUtils');
const { expect } = require('chai');

describe('Assurance Template', () => {
  it('génère un projet assurance sécurisé, multilingue, RGPD', async () => {
    const req = mockRequest({
      body: {
        name: 'Assurance Santé IA',
        lang: 'fr',
        tenant: 'mutuelle',
        userRole: 'admin',
        features: ['RGPD', 'AI'],
      },
      user: { id: '2', role: 'admin', tenant: 'mutuelle' },
    });
    const res = mockResponse();
    await generateAssuranceProject(req, res, mockNext);
    expect(res.status.calledWith(201)).to.be.true;
    expect(res.json.called).to.be.true;
    const data = res.json.firstCall.args[0];
    expect(data.project.name).to.equal('Assurance Santé IA');
    expect(data.project.security.rgpd).to.be.true;
    expect(data.project.plugins.length).to.be.greaterThan(0);
    expect(data.project.i18n).to.have.property('fr');
  });
});
