// Index des tests JS
globalThis.tests = globalThis.tests || {};
// ...importez ici tous les tests du dossier

describe('dummy', () => { it('should pass', () => { expect(true).toBe(true); }); });

const { assetTypes, getAssetConfig } = require('../../../../blockchain/assets.config');
describe('Assets', () => {
  it('liste les types d’assets supportés', () => {
    expect(assetTypes.map(a => a.type)).toContain('NFT');
    expect(assetTypes.map(a => a.type)).toContain('ERC20');
  });
  it('récupère la config d’un asset NFT', () => {
    const nft = getAssetConfig('NFT');
    expect(nft).toBeDefined();
    expect(nft.type).toBe('NFT');
  });
});
