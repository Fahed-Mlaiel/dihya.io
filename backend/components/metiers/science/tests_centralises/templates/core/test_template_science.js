// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderscienceTemplateUltra, validatescienceTemplateUltra } = require('./template_science');

describe('Templates Core Central Tests', () => {
    it('should render a valid science template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderscienceTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderscienceTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderscienceTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderscienceTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderscienceTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate science template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validatescienceTemplateUltra(data)).toBe(true);
    });

    it('should invalidate science template (missing id/name or RGPD)', () => {
        expect(validatescienceTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validatescienceTemplateUltra({ id: '4' })).toBe(false);
        expect(validatescienceTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validatescienceTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderscienceTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
