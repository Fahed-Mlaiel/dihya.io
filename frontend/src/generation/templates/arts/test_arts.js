// test_arts.js
// Test complet pour le template arts (gestion IA, VR, AR, multilingue, sécurité, audit, plugins, etc.)
// @see ./template.js

const { generateArtsProject } = require('./template');
const { mockRequest, mockResponse, mockNext } = require('../../../../utils/testUtils');
const { expect } = require('chai');

describe('Arts Template', () => {
  it('génère un projet arts complet, multilingue, sécurisé', async () => {
    const req = mockRequest({
      body: {
        name: 'Projet VR Amazigh',
        lang: 'fr',
        tenant: 'demo',
        userRole: 'admin',
        features: ['VR', 'AR', 'AI'],
      },
      user: { id: '1', role: 'admin', tenant: 'demo' },
    });
    const res = mockResponse();
    await generateArtsProject(req, res, mockNext);
    expect(res.status.calledWith(201)).to.be.true;
    expect(res.json.called).to.be.true;
    const data = res.json.firstCall.args[0];
    expect(data.project.name).to.equal('Projet VR Amazigh');
    expect(data.project.features).to.include('VR');
    expect(data.project.lang).to.equal('fr');
    expect(data.project.security.audit).to.be.true;
    expect(data.project.plugins.length).to.be.greaterThan(0);
  });
});
