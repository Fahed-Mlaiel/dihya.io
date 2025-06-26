const ServicesIndex = require('../../../../../../blockchain/services/index');
describe('ServicesIndex (deploy)', () => {
  it('déploie un smart contract ERC20', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ action: 'deploy', contract: 'ERC20', params: { name: 'Token', symbol: 'TKN' } });
    expect(result).toBeDefined();
    expect(result.contract).toBe('ERC20');
  });
  it('déploie un smart contract NFT', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ action: 'deploy', contract: 'NFT', params: { name: 'NFT Alpha' } });
    expect(result).toBeDefined();
    expect(result.contract).toBe('NFT');
  });
});
