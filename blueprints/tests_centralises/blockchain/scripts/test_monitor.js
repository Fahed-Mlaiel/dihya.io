const { monitorAsset } = require('../../../../blueprints/blockchain/scripts');

describe('monitorAsset', () => {
  it('retourne un statut healthy pour un asset valide', () => {
    const asset = { id: 'nft-001', type: 'NFT' };
    const status = monitorAsset(asset);
    expect(status.status).toBe('healthy');
    expect(status.details).toContain('nft-001');
  });
  it('retourne unknown pour asset sans id', () => {
    const status = monitorAsset({ type: 'NFT' });
    expect(status.status).toBe('unknown');
    expect(status.reason).toBe('ID manquant');
  });
});
