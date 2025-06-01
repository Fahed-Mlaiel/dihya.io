// test_crypto.js
// Test complet pour le template crypto (sécurité, RGPD, plugins, multilingue, audit, etc.)
const { generateCryptoProject } = require('./template');
const { mockRequest, mockResponse, mockNext } = require('../../../../utils/testUtils');
const { expect } = require('chai');

describe('Crypto Template', () => {
  it('génère un projet crypto sécurisé, multilingue, RGPD', async () => {
    const req = mockRequest({
      body: {
        name: 'CryptoChain',
        lang: 'fa',
        tenant: 'blockchain',
        userRole: 'admin',
        features: ['RGPD', 'AI'],
      },
      user: { id: '7', role: 'admin', tenant: 'blockchain' },
    });
    const res = mockResponse();
    await generateCryptoProject(req, res, mockNext);
    expect(res.status.calledWith(201)).to.be.true;
    expect(res.json.called).to.be.true;
    const data = res.json.firstCall.args[0];
    expect(data.project.name).to.equal('CryptoChain');
    expect(data.project.security.rgpd).to.be.true;
    expect(data.project.plugins.length).to.be.greaterThan(0);
    expect(data.project.i18n).to.have.property('fa');
  });
});
