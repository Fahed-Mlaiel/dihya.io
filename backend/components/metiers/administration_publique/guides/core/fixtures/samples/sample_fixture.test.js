// sample_fixture.test.js - Test unitaire pour sample_fixture.js (guides/core/fixtures)
const sampleFixture = require('./sample_fixture');
describe('guides/core/fixtures/sample_fixture.js', () => {
  it('doit exposer un objet sample correct', () => {
    expect(sampleFixture.sample).toBeDefined();
    expect(sampleFixture.sample.name).toBe('Sample Guide Fixture');
    expect(sampleFixture.sample.type).toBe('guide');
    expect(sampleFixture.sample.status).toBe('active');
  });
});
