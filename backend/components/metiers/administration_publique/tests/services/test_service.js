// test_service.js - Tests unitaires pour le module services.js du domaine Threed
// Respecte la logique métier, la structure modulaire, et le cahier des charges

const services = require('./services.js');

describe('Services 3D - JS', () => {
  test('get3DAssetById retourne un asset structuré', async () => {
    const asset = await services.get3DAssetById('asset_test');
    expect(asset).toHaveProperty('id', 'asset_test');
    expect(asset).toHaveProperty('name');
    expect(asset).toHaveProperty('type', '3D');
    expect(asset).toHaveProperty('createdAt');
  });

  test('create3DAsset crée un asset avec les bons champs', async () => {
    const data = { name: 'Test Asset', type: '3D' };
    const asset = await services.create3DAsset(data);
    expect(asset).toHaveProperty('id');
    expect(asset).toHaveProperty('name', 'Test Asset');
    expect(asset).toHaveProperty('type', '3D');
    expect(asset).toHaveProperty('createdAt');
  });

  test('list3DAssets retourne une liste d’assets', async () => {
    const assets = await services.list3DAssets();
    expect(Array.isArray(assets)).toBe(true);
    expect(assets.length).toBeGreaterThan(0);
    assets.forEach(asset => {
      expect(asset).toHaveProperty('id');
      expect(asset).toHaveProperty('name');
      expect(asset).toHaveProperty('type', '3D');
    });
  });
});
