// test_btp.js
// Test complet pour le template BTP (sécurité, RGPD, plugins, multilingue, audit, etc.)
const { generateBTPProject } = require('./template');
const { mockRequest, mockResponse, mockNext } = require('../../../../utils/testUtils');
const { expect } = require('chai');

describe('BTP Template', () => {
  it('génère un projet BTP sécurisé, multilingue, RGPD', async () => {
    const req = mockRequest({
      body: {
        name: 'BTP Smart',
        lang: 'de',
        tenant: 'btp',
        userRole: 'admin',
        features: ['RGPD', 'AI'],
      },
      user: { id: '5', role: 'admin', tenant: 'btp' },
    });
    const res = mockResponse();
    await generateBTPProject(req, res, mockNext);
    expect(res.status.calledWith(201)).to.be.true;
    expect(res.json.called).to.be.true;
    const data = res.json.firstCall.args[0];
    expect(data.project.name).to.equal('BTP Smart');
    expect(data.project.security.rgpd).to.be.true;
    expect(data.project.plugins.length).to.be.greaterThan(0);
    expect(data.project.i18n).to.have.property('de');
  });
});
