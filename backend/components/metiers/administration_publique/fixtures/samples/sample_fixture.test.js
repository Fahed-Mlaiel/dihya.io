// sample_fixture.test.js - Test unitaire pour sample_fixture.js (helpers/core/samples)
const sampleFixture = require('./sample_fixture');
describe('helpers/core/samples/sample_fixture.js', () => {
  it('doit exposer un objet sample correct', () => {
    expect(sampleFixture.sample).toBeDefined();
    expect(sampleFixture.sample.name).toBe('Sample Helper');
    expect(sampleFixture.sample.type).toBe('helper');
    expect(sampleFixture.sample.status).toBe('active');
  });
});
