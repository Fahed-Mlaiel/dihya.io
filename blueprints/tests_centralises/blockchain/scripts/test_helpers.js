const { isValidAsset, generateAssetId } = require('../../../../blueprints/blockchain/scripts');

describe('isValidAsset', () => {
  it('valide un asset avec id', () => {
    expect(isValidAsset({ id: 'nft-001' })).toBe(true);
  });
  it('rejette un asset sans id', () => {
    expect(isValidAsset({})).toBe(false);
  });
});

describe('generateAssetId', () => {
  it('génère un id unique commençant par nft-', () => {
    const id = generateAssetId();
    expect(id.startsWith('nft-')).toBe(true);
    expect(id.length).toBeGreaterThan(4);
  });
});
