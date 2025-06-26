const { WebhookService } = require('../../../../blockchain/services');
describe('WebhookService', () => {
  it('crée un webhook pour un event blockchain', () => {
    const service = new WebhookService();
    const webhook = service.createWebhook({ event: 'tx', url: 'https://example.com/webhook' });
    expect(webhook.active).toBe(true);
  });
  it('déclenche un webhook sur event', () => {
    const service = new WebhookService();
    const result = service.triggerWebhook('tx', { hash: '0xabc' });
    expect(result.status).toBe('delivered');
  });
});
