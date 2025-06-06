// Test JS pour le template rapport_score.html.j2
const fs = require('fs');
test('Le template rapport_score existe', () => {
  expect(fs.existsSync(__dirname + '/rapport_score.html.j2')).toBe(true);
});
