// test_utils.js – Test des utilitaires Environnement (Node.js/Jest)
const audit = require('../utils/audit');
const i18n = require('../utils/i18n');
const validators = require('../utils/validators');

describe('Utils Environnement', () => {
  it('auditEnvironnement doit retourner un score', () => {
    const result = audit.auditEnvironnement({ statut: 'actif' });
    expect(result).toHaveProperty('score');
    expect(result.score).toBeGreaterThan(0);
  });
  it('i18n doit traduire le texte', () => {
    expect(i18n('Test', 'fr')).toMatch('[FR]');
    expect(i18n('Test', 'en')).toMatch('[EN]');
  });
  it('validators doit valider une entité correcte', () => {
    expect(() => validators({ nom: 'ok', statut: 'actif' })).not.toThrow();
  });
  it('validators doit refuser une entité sans nom', () => {
    expect(() => validators({ statut: 'actif' })).toThrow();
  });
});
