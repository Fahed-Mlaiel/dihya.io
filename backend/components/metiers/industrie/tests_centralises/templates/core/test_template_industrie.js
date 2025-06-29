// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderindustrieTemplateUltra, validateindustrieTemplateUltra } = require('./template_industrie');

describe('Templates Core Central Tests', () => {
    it('should render a valid industrie template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderindustrieTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderindustrieTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderindustrieTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderindustrieTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderindustrieTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate industrie template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validateindustrieTemplateUltra(data)).toBe(true);
    });

    it('should invalidate industrie template (missing id/name or RGPD)', () => {
        expect(validateindustrieTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validateindustrieTemplateUltra({ id: '4' })).toBe(false);
        expect(validateindustrieTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validateindustrieTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderindustrieTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
