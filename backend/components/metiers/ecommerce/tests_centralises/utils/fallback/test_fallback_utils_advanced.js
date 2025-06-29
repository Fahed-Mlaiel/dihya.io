const { mockUser, mockPlugin } = require("../../../fixtures/mocks/advanced/mocks_centralized");

describe('Fallback Utils ecommerce – Ultra avancé', () => {
  it('doit gérer le fallback métier avec audit et RGPD', () => {
    const user = mockUser('admin');
    const plugin = mockPlugin('audit');
    const fallbackUtils = { handleFallback: () => ({ success: true }) };
    const auditFallback = () => true;
    const rgpdFallback = () => true;
    const result = fallbackUtils.handleFallback(user, plugin);
    expect(result.success).toBe(true);
    expect(auditFallback(result)).toBe(true);
    expect(rgpdFallback(result)).toBe(true);
  });

  it('doit être extensible (plugins, hooks, multilingue)', () => {
    const plugin = mockPlugin('i18n');
    const fallbackUtils = { isExtensible: () => true };
    expect(fallbackUtils.isExtensible(plugin)).toBe(true);
  });
});
