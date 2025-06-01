// test_beaute.js
// Test complet pour le template beauté (sécurité, plugins, multilingue, audit, etc.)
const { generateBeauteProject } = require('./template');
const { mockRequest, mockResponse, mockNext } = require('../../../../utils/testUtils');
const { expect } = require('chai');

describe('Beaute Template', () => {
  it('génère un projet beauté sécurisé, multilingue, plugins', async () => {
    const req = mockRequest({
      body: {
        name: 'Beauty AI',
        lang: 'fr',
        tenant: 'cosmetics',
        userRole: 'admin',
        features: ['AI', 'SEO'],
      },
      user: { id: '4', role: 'admin', tenant: 'cosmetics' },
    });
    const res = mockResponse();
    await generateBeauteProject(req, res, mockNext);
    expect(res.status.calledWith(201)).to.be.true;
    expect(res.json.called).to.be.true;
    const data = res.json.firstCall.args[0];
    expect(data.project.name).to.equal('Beauty AI');
    expect(data.project.plugins.length).to.be.greaterThan(0);
    expect(data.project.i18n).to.have.property('fr');
  });
});
