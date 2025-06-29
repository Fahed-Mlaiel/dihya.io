const { IndexerService } = require('../../../../blockchain/services');
describe('IndexerService', () => {
  it('indexe un nouveau bloc', () => {
    const service = new IndexerService();
    const result = service.indexBlock({ number: 123, hash: '0xabc' });
    expect(result.success).toBe(true);
  });
  it('recherche un asset par ID', () => {
    const service = new IndexerService();
    const asset = service.findAssetById('asset-001');
    expect(asset).toBeDefined();
  });
});
