const examples = require('../../../../blockchain/examples');
describe('examples', () => {
  it('exécute un exemple d’intégration web3', () => {
    const result = examples.runExample('web3-integration');
    expect(result.success).toBe(true);
  });
  it('gère un cas limite d’exemple incomplet', () => {
    const result = examples.runExample('incomplete');
    expect(result.success).toBe(false);
  });
});
