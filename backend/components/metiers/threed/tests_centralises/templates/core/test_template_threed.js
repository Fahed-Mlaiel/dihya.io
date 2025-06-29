// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderthreedTemplateUltra, validatethreedTemplateUltra } = require('./template_threed');

describe('Templates Core Central Tests', () => {
    it('should render a valid threed template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderthreedTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderthreedTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderthreedTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderthreedTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderthreedTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate threed template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validatethreedTemplateUltra(data)).toBe(true);
    });

    it('should invalidate threed template (missing id/name or RGPD)', () => {
        expect(validatethreedTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validatethreedTemplateUltra({ id: '4' })).toBe(false);
        expect(validatethreedTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validatethreedTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderthreedTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
