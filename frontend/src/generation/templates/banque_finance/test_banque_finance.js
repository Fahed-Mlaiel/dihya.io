// test_banque_finance.js
// Test complet pour le template banque/finance (sécurité, RGPD, plugins, multilingue, audit, etc.)
const { generateBanqueFinanceProject } = require('./template');
const { mockRequest, mockResponse, mockNext } = require('../../../../utils/testUtils');
const { expect } = require('chai');

describe('BanqueFinance Template', () => {
  it('génère un projet banque/finance sécurisé, multilingue, RGPD', async () => {
    const req = mockRequest({
      body: {
        name: 'Fintech IA',
        lang: 'en',
        tenant: 'fintech',
        userRole: 'admin',
        features: ['RGPD', 'AI'],
      },
      user: { id: '3', role: 'admin', tenant: 'fintech' },
    });
    const res = mockResponse();
    await generateBanqueFinanceProject(req, res, mockNext);
    expect(res.status.calledWith(201)).to.be.true;
    expect(res.json.called).to.be.true;
    const data = res.json.firstCall.args[0];
    expect(data.project.name).to.equal('Fintech IA');
    expect(data.project.security.rgpd).to.be.true;
    expect(data.project.plugins.length).to.be.greaterThan(0);
    expect(data.project.i18n).to.have.property('en');
  });
});
