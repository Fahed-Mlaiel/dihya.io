// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderagricultureTemplateUltra, validateagricultureTemplateUltra } = require('./template_agriculture');

describe('Templates Core Central Tests', () => {
    it('should render a valid agriculture template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderagricultureTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderagricultureTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderagricultureTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderagricultureTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderagricultureTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate agriculture template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validateagricultureTemplateUltra(data)).toBe(true);
    });

    it('should invalidate agriculture template (missing id/name or RGPD)', () => {
        expect(validateagricultureTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validateagricultureTemplateUltra({ id: '4' })).toBe(false);
        expect(validateagricultureTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validateagricultureTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderagricultureTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
