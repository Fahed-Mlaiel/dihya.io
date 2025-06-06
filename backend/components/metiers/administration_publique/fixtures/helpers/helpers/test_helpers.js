// test_helpers.js – Tests unitaires et edge cases helpers JS
const helpers = require('./helpers');

test('getModelById returns correct model', () => {
  const fixtures = [{ id: 'a', name: 'A' }, { id: 'b', name: 'B' }];
  expect(helpers.getModelById(fixtures, 'b')).toEqual({ id: 'b', name: 'B' });
});

test('anonymizeFixture anonymizes sensitive fields', () => {
  const fixture = { id: 'x', name: 'Secret', owner: 'user1' };
  const anonymized = helpers.anonymizeFixture(fixture);
  expect(anonymized.name).toBe('anonymized');
  expect(anonymized.owner).toBeNull();
});

test('auditFixture returns correct audit info', () => {
  const fixture = { name: 'A', vertices: [1,2], description: 'desc' };
  const audit = helpers.auditFixture(fixture);
  expect(audit.hasName).toBe(true);
  expect(audit.hasVertices).toBe(true);
  expect(audit.isAccessible).toBe(true);
});
