// sample_fixture.test.js - Test unitaire pour sample_fixture.js (mocks/samples)
const sampleFixture = require('./sample_fixture');
describe('mocks/samples/sample_fixture.js', () => {
  it('doit exposer un objet sample correct', () => {
    expect(sampleFixture.sample).toBeDefined();
    expect(sampleFixture.sample.name).toBe('Sample Mock');
    expect(sampleFixture.sample.type).toBe('mock');
    expect(sampleFixture.sample.status).toBe('active');
  });
});
