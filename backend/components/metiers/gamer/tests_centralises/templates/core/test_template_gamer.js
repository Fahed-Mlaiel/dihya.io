// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { rendergamerTemplateUltra, validategamerTemplateUltra } = require('./template_gamer');

describe('Templates Core Central Tests', () => {
    it('should render a valid gamer template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = rendergamerTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => rendergamerTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => rendergamerTemplateUltra({ id: '1' })).toThrow();
        expect(() => rendergamerTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = rendergamerTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate gamer template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validategamerTemplateUltra(data)).toBe(true);
    });

    it('should invalidate gamer template (missing id/name or RGPD)', () => {
        expect(validategamerTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validategamerTemplateUltra({ id: '4' })).toBe(false);
        expect(validategamerTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validategamerTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = rendergamerTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
