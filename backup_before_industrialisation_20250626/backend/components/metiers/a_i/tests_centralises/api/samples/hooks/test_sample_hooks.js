// test_sample_hooks.js – Test ultra avancé des samples hooks API A_I (centralisé)

const { sampleHookUltra } = require('../../../api/samples/hooks');

describe('Samples Hooks API A_I', () => {
  it('doit exécuter le hook ultra avancé avant action', () => {
    const event = 'before_create';
    const data = { name: 'UltraCube', status: 'active' };
    const result = sampleHookUltra(event, data);
    expect(result.event).toBe(event);
    expect(result.data).toEqual(data);
    expect(result.hooked).toBe(true);
  });

  it('doit exécuter le hook ultra avancé après action', () => {
    const event = 'after_update';
    const data = { name: 'UltraCubeV2', status: 'inactive' };
    const result = sampleHookUltra(event, data);
    expect(result.event).toBe(event);
    expect(result.data).toEqual(data);
    expect(result.hooked).toBe(true);
  });
});
