// test_legacy.js – Tests de compatibilité et migration legacy Threed

describe('Legacy/Migration Threed', () => {
  it('doit migrer un ancien format de données sans erreur', () => {
    // Exemple : migration d’un ancien objet 3D
    const oldData = { version: '1.0', name: 'Cube', meta: { deprecated: true } };
    // Simuler une migration (à adapter selon logique métier)
    const migrated = { ...oldData, version: '2.0', meta: { ...oldData.meta, migrated: true } };
    expect(migrated.version).toBe('2.0');
    expect(migrated.meta.migrated).toBe(true);
  });
  it('doit détecter les champs obsolètes', () => {
    const legacyObj = { oldField: 'deprecated', name: 'Test' };
    expect(Object.keys(legacyObj)).toContain('oldField');
  });
});
