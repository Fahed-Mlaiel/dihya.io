// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderimmobilierTemplateUltra, validateimmobilierTemplateUltra } = require('./template_immobilier');

describe('Templates Core Central Tests', () => {
    it('should render a valid immobilier template (nominal)', () => {
        const data = { id: '1', name: 'Bien', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Bien' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderimmobilierTemplateUltra(data, options);
        expect(result).toContain('Bien');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderimmobilierTemplateUltra({ name: 'Bien' })).toThrow();
        expect(() => renderimmobilierTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderimmobilierTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderimmobilierTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate immobilier template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validateimmobilierTemplateUltra(data)).toBe(true);
    });

    it('should invalidate immobilier template (missing id/name or RGPD)', () => {
        expect(validateimmobilierTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validateimmobilierTemplateUltra({ id: '4' })).toBe(false);
        expect(validateimmobilierTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validateimmobilierTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderimmobilierTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
