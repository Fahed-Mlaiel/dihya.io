// sample_fixture.test.js - Test unitaire pour sample_fixture.js (guides/core/accessibility/samples)
const sampleFixture = require('./sample_fixture');
describe('guides/core/accessibility/samples/sample_fixture.js', () => {
  it('doit exposer un objet sample correct', () => {
    expect(sampleFixture.sample).toBeDefined();
    expect(sampleFixture.sample.name).toBe('Sample Accessibility Guide');
    expect(sampleFixture.sample.type).toBe('accessibility');
    expect(sampleFixture.sample.status).toBe('active');
  });
});
