// __init__.test.js – Test d'import du point d'entrée users (fixtures/core/samples)
const { sampleUsersUltra } = require('./sample_users');
test('import sampleUsersUltra', () => {
  expect(typeof sampleUsersUltra).toBe('function');
});
