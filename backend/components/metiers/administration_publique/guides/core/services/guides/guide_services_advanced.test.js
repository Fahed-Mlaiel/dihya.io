// Test unitaire pour guide_services_advanced.md (JS)
test('guide_services_advanced.md existe et contient Guide avancé', () => {
  const fs = require('fs');
  const content = fs.readFileSync('guide_services_advanced.md', 'utf-8');
  expect(content).toContain('Guide avancé');
});
