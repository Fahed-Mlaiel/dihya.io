// __init__.test.js - Test d’intégration du point d’entrée JS pour les tests services Threed
// Vérifie que le module __init__.js s’importe et expose bien les helpers attendus

const entry = require('./__init__.js');

describe('Entrée JS tests services Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
    expect(typeof entry.mock3DService).toBe('function');
    const mock = entry.mock3DService();
    expect(mock).toHaveProperty('id');
    expect(mock).toHaveProperty('name');
    expect(mock).toHaveProperty('status');
    expect(mock).toHaveProperty('environment');
    expect(mock).toHaveProperty('compliance');
  });
});
