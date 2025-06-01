// Beispiel-Unit-Test für Validatoren
const { validateInput } = require('./template');

test('validateInput gibt true für gültige Eingabe zurück', () => {
  expect(validateInput('test')).toBe(true);
});

test('validateInput gibt false für ungültige Eingabe zurück', () => {
  expect(validateInput('')).toBe(false);
});
