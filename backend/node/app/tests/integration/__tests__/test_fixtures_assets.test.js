// Test d'intégration automatisée des fixtures générées (Node.js/Jest)
const users = require('../../../assets/datasets/fixtures/users_sample_fixture');
const transactions = require('../../../assets/datasets/fixtures/transactions_sample_fixture');
const audits = require('../../../assets/datasets/fixtures/audit_events_sample_fixture');

describe('Fixtures Générées - Intégration', () => {
  test('users_sample_fixture structure', () => {
    users.forEach(user => {
      expect(user).toHaveProperty('username');
      expect(user).toHaveProperty('email');
      expect(user).toHaveProperty('lang');
      expect(['fr', 'en', 'ar', 'kab']).toContain(user.lang);
      expect(user).toHaveProperty('role');
    });
  });

  test('transactions_sample_fixture structure', () => {
    transactions.forEach(tx => {
      expect(tx).toHaveProperty('id');
      expect(tx).toHaveProperty('amount');
      expect(tx).toHaveProperty('currency');
      expect(tx).toHaveProperty('status');
      expect(tx).toHaveProperty('user_id');
      expect(['fr', 'en', 'ar', 'kab']).toContain(tx.lang);
    });
  });

  test('audit_events_sample_fixture structure', () => {
    audits.forEach(event => {
      expect(event).toHaveProperty('timestamp');
      expect(event).toHaveProperty('event');
      expect(event).toHaveProperty('user');
      expect(event).toHaveProperty('action');
      expect(event).toHaveProperty('result');
      expect(['fr', 'en', 'ar', 'kab']).toContain(event.lang);
    });
  });
});
