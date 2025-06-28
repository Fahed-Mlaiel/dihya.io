/* global jest, console */
/* global console */
const generateChecklist = require('../../../../../legacy/documentation/checklists/checklist_generator');

// Test ultra avancé pour la checklist documentation JS
describe('Checklist Doc', () => {
  it('doit valider la checklist documentation', () => {
    const items = [
      'Documentation technique complète',
      'Documentation fonctionnelle complète',
      'Modèles de guides prêts à l’emploi',
      'Changelog documenté',
      'Accessibilité et multilingue'
    ];
    // Capture console.log
    const logs = [];
    const spy = jest.spyOn(console, 'log').mockImplementation(msg => logs.push(msg));
    generateChecklist(items);
    expect(logs[0]).toMatch(/Checklist générée/);
    expect(logs.length).toBe(items.length + 1);
    items.forEach(item => {
      expect(logs.some(l => l.includes(item))).toBe(true);
    });
    spy.mockRestore();
  });
  it('doit gérer les cas limites (liste vide)', () => {
    const logs = [];
    const spy = jest.spyOn(console, 'log').mockImplementation(msg => logs.push(msg));
    generateChecklist([]);
    expect(logs[0]).toMatch(/Checklist générée/);
    expect(logs.length).toBe(1);
    spy.mockRestore();
  });
});
