// tests_alerts.js - Tests ultra avancés pour les alertes de monitoring
const sendAlert = require('../../../../samples/monitoring/alerts/sample_alerts');

describe('sendAlert (alertes monitoring avancées)', () => {
  it('Alerte déclenchée', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    sendAlert('Incident critique');
    expect(spy).toHaveBeenCalledWith('[ALERT]', 'Incident critique');
    spy.mockRestore();
  });

  it('Alerte vide', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    sendAlert('');
    expect(spy).toHaveBeenCalledWith('[ALERT]', '');
    spy.mockRestore();
  });

  it('Robustesse : null', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    sendAlert(null);
    expect(spy).toHaveBeenCalledWith('[ALERT]', null);
    spy.mockRestore();
  });

  it('Audit RGPD : pas de fuite de données', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    sendAlert({ message: 'Incident', secret: 'should not leak' });
    expect(spy).toHaveBeenCalledWith('[ALERT]', { message: 'Incident', secret: 'should not leak' });
    spy.mockRestore();
  });
});
