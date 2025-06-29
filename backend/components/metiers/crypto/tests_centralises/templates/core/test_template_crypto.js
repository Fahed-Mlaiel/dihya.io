// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { rendercryptoTemplateUltra, validatecryptoTemplateUltra } = require('./template_crypto');

describe('Templates Core Central Tests', () => {
    it('should render a valid crypto template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = rendercryptoTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => rendercryptoTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => rendercryptoTemplateUltra({ id: '1' })).toThrow();
        expect(() => rendercryptoTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = rendercryptoTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate crypto template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validatecryptoTemplateUltra(data)).toBe(true);
    });

    it('should invalidate crypto template (missing id/name or RGPD)', () => {
        expect(validatecryptoTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validatecryptoTemplateUltra({ id: '4' })).toBe(false);
        expect(validatecryptoTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validatecryptoTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = rendercryptoTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
