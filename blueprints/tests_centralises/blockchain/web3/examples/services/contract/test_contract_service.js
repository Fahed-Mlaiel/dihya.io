const ServicesIndex = require('../../../../../../blockchain/services/index');
describe('ServicesIndex (contract)', () => {
  it('appelle une fonction de smart contract', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ action: 'call', contract: 'ERC20', method: 'balanceOf', params: { address: '0x123' } });
    expect(result).toBeDefined();
    expect(result.method).toBe('balanceOf');
  });
  it('écoute un event de smart contract', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ action: 'listen', contract: 'NFT', event: 'Transfer' });
    expect(result).toBeDefined();
    expect(result.event).toBe('Transfer');
  });
});
