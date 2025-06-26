// test_sample_core.js – Test ultra avancé des samples cœur métier API Agriculture (centralisé)

const { sampleCoreLogic } = require('../../../api/samples/core');

describe('Samples Cœur métier API Agriculture', () => {
  it('doit exécuter la logique cœur métier ultra avancée', () => {
    const data = { input: 'test', flag: true };
    const result = sampleCoreLogic(data);
    expect(result.core_processed).toBe(true);
    expect(result.input).toEqual(data);
    expect(result.status).toBe('ok');
  });
});
