// Tests avancés pour les services threed
const { runService, getServiceStatus } = require('../../api/services');
describe('Services threed', () => {
  it('doit exécuter le service de notification sans erreur', async () => {
    const result = await runService('notification', { message: 'test' });
    expect(result.success).toBe(true);
  });
  it('doit retourner le statut du service de monitoring', () => {
    const status = getServiceStatus('monitoring');
    expect(['running', 'stopped']).toContain(status);
  });
});
