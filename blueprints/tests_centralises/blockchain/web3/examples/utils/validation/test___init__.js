const { validators } = require('../../../../../../blockchain/utils/index');
describe('validators (validation)', () => {
  it('valide une adresse Ethereum correcte', () => {
    expect(validators.isValidAddress('0x1234567890123456789012345678901234567890')).toBe(true);
  });
  it('rejette une adresse Ethereum incorrecte', () => {
    expect(validators.isValidAddress('0x1234')).toBe(false);
  });
  it('valide une signature hex', () => {
    expect(validators.isValidSignature('0xabcdef')).toBe(true);
  });
});
