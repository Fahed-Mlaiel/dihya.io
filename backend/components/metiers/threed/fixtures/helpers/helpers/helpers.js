// helpers/helpers.js – Helpers métiers ultra avancés (JS)
module.exports = {
  getModelById: (fixtures, id) => fixtures.find(f => f.id === id) || null,
  anonymizeFixture: (fixture) => {
    const anonymized = { ...fixture, name: 'anonymized', owner: null };
    return anonymized;
  },
  auditFixture: (fixture) => ({
    hasName: !!fixture.name,
    hasVertices: !!fixture.vertices,
    isAccessible: typeof fixture.description === 'string',
  })
};
