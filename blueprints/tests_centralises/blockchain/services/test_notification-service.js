const { NotificationService } = require('../../../../blockchain/services');
describe('NotificationService', () => {
  it('envoie une notification à un utilisateur', () => {
    const service = new NotificationService();
    const notif = service.sendNotification({ userId: 'user1', message: 'Test' });
    expect(notif.status).toBe('sent');
  });
  it('gère les abonnements aux notifications', () => {
    const service = new NotificationService();
    const sub = service.subscribe('user1', 'blockchain_alerts');
    expect(sub.active).toBe(true);
  });
});
