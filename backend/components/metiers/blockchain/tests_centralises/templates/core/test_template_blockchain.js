// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderblockchainTemplateUltra, validateblockchainTemplateUltra } = require('./template_blockchain');

describe('Templates Core Central Tests', () => {
    it('should render a valid blockchain template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderblockchainTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderblockchainTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderblockchainTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderblockchainTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderblockchainTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate blockchain template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validateblockchainTemplateUltra(data)).toBe(true);
    });

    it('should invalidate blockchain template (missing id/name or RGPD)', () => {
        expect(validateblockchainTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validateblockchainTemplateUltra({ id: '4' })).toBe(false);
        expect(validateblockchainTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validateblockchainTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderblockchainTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
