const { migrateAsset } = require('../../../../blueprints/blockchain/scripts');

describe('migrateAsset', () => {
  it('migre un asset NFT de v1 à v2', () => {
    const asset = { id: 'nft-001', type: 'NFT' };
    const result = migrateAsset(asset, { from: 'v1', to: 'v2' });
    expect(result.migrated).toBe(true);
    expect(result.from).toBe('v1');
    expect(result.to).toBe('v2');
  });
  it('migre avec options par défaut', () => {
    const asset = { id: 'nft-002', type: 'NFT' };
    const result = migrateAsset(asset);
    expect(result.migrated).toBe(true);
    expect(result.from).toBe('v1');
    expect(result.to).toBe('v2');
  });
  it('rejette un asset sans id', () => {
    expect(() => migrateAsset({ type: 'NFT' })).toThrow('Asset à migrer invalide');
  });
});
