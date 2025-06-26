const { auditAsset } = require('../../../../blueprints/blockchain/scripts');

describe('auditAsset', () => {
  it('valide un asset NFT conforme', () => {
    const asset = { id: 'nft-001', type: 'NFT' };
    const report = auditAsset(asset);
    expect(report.valid).toBe(true);
    expect(report.score).toBe(100);
    expect(report.reason).toBeNull();
  });
  it('détecte un asset non conforme', () => {
    const asset = { id: 'bad-001', type: 'NFT' };
    const report = auditAsset(asset);
    expect(report.valid).toBe(false);
    expect(report.score).toBe(60);
    expect(report.reason).toBe('Format ID incorrect');
  });
  it('rejette un asset sans id', () => {
    const report = auditAsset({ type: 'NFT' });
    expect(report.valid).toBe(false);
    expect(report.reason).toBe('ID manquant');
  });
});
