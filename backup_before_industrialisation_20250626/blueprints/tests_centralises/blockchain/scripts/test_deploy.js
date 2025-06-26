const { deployAsset } = require('../../../../blueprints/blockchain/scripts');

describe('deployAsset', () => {
  it('déploie un asset NFT valide', () => {
    const asset = { id: 'nft-001', type: 'NFT' };
    const result = deployAsset(asset);
    expect(result.success).toBe(true);
    expect(result.txHash).toContain('nft-001');
    expect(result.network).toBe('testnet');
  });
  it('déploie en mode simulation', () => {
    const asset = { id: 'nft-002', type: 'NFT' };
    const result = deployAsset(asset, { simulate: true, network: 'mainnet' });
    expect(result.simulated).toBe(true);
    expect(result.network).toBe('mainnet');
  });
  it('rejette un asset sans id', () => {
    expect(() => deployAsset({ type: 'NFT' })).toThrow('Asset ou contrat invalide');
  });
});
