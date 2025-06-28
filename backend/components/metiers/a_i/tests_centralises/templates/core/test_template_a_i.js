// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { rendera_iTemplateUltra, validatea_iTemplateUltra } = require('./template_a_i');

describe('Templates Core Central Tests', () => {
    it('should render a valid a_i template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = rendera_iTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => rendera_iTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => rendera_iTemplateUltra({ id: '1' })).toThrow();
        expect(() => rendera_iTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = rendera_iTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate a_i template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validatea_iTemplateUltra(data)).toBe(true);
    });

    it('should invalidate a_i template (missing id/name or RGPD)', () => {
        expect(validatea_iTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validatea_iTemplateUltra({ id: '4' })).toBe(false);
        expect(validatea_iTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validatea_iTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = rendera_iTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
