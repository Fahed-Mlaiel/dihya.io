const { OracleService } = require('../../../../blockchain/services');
describe('OracleService', () => {
  it('récupère un prix on-chain', async () => {
    const service = new OracleService();
    const price = await service.getPrice('ETH/USD');
    expect(typeof price).toBe('number');
    expect(price).toBeGreaterThan(0);
  });
  it('met à jour une donnée off-chain', async () => {
    const service = new OracleService();
    const result = await service.updateData('BTC/USD', 65000);
    expect(result.success).toBe(true);
  });
});
