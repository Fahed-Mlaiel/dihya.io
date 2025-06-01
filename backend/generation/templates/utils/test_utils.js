// Test für Utility-Funktionen

describe('Utility-Funktionen', () => {
  it('sollte die execute-Funktion korrekt ausführen', () => {
    const util = require('./template');
    expect(util.execute(1, 2, 3)).toEqual([1, 2, 3]);
  });

  // Beispiel-Unit-Test für Utility-Funktionen
  const { sum } = require('./utils');

  test('sum addiert zwei Zahlen korrekt', () => {
    expect(sum(2, 3)).toBe(5);
  });
});
