// sample_users.test.js – Test ultra avancé pour sampleUsers (JS)
const sampleUsersUltra = require('./sample_users');
test('sampleUsersUltra fonctionne sans erreur', () => {
  expect(() => sampleUsersUltra()).not.toThrow();
});
