// Test JS pour le template sample_template.html.j2
const fs = require('fs');
test('Le template sample_template existe', () => {
  expect(fs.existsSync(__dirname + '/sample_template.html.j2')).toBe(true);
});
