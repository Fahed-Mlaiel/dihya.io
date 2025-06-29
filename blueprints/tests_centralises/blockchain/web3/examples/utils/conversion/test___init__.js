const { txUtils } = require('../../../../../../blockchain/utils/index');
describe('txUtils (conversion)', () => {
  it('convertit un montant ETH en Wei', () => {
    expect(txUtils.ethToWei('1')).toBe('1000000000000000000');
  });
  it('convertit un montant Wei en ETH', () => {
    expect(txUtils.weiToEth('1000000000000000000')).toBe('1');
  });
  it('convertit un hash hex en buffer', () => {
    const buf = txUtils.hexToBuffer('0x1234');
    expect(Buffer.isBuffer(buf)).toBe(true);
  });
});
