/* global jest, console */
// tests_logger.js - Tests ultra avancés pour le logger
const log = require('../../../../samples/helpers/logger/sample_logger.js');
describe('Logger avancé', () => {
  it('écrit un message simple', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    log('test');
    expect(spy).toHaveBeenCalledWith('[LOGGER]', 'test');
    spy.mockRestore();
  });
  it('gère les messages vides', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    log('');
    expect(spy).toHaveBeenCalledWith('[LOGGER]', '');
    spy.mockRestore();
  });
  it('ne log pas de données sensibles (RGPD)', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    const sensitive = { password: 'secret', email: 'user@dihya.io' };
    log(sensitive);
    const calls = spy.mock.calls.map(args => args.join(' ')).join(' ');
    expect(calls).not.toMatch(/secret|user@dihya.io/);
    spy.mockRestore();
  });
  it('robustesse : accepte tout type', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    log(null);
    log(undefined);
    log(123);
    expect(spy).toHaveBeenCalledTimes(3);
    spy.mockRestore();
  });
});
