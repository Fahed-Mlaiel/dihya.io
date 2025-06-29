// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderhotellerieTemplateUltra, validatehotellerieTemplateUltra } = require('./template_hotellerie');

describe('Templates Core Central Tests', () => {
    it('should render a valid hotellerie template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderhotellerieTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderhotellerieTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderhotellerieTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderhotellerieTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderhotellerieTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate hotellerie template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validatehotellerieTemplateUltra(data)).toBe(true);
    });

    it('should invalidate hotellerie template (missing id/name or RGPD)', () => {
        expect(validatehotellerieTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validatehotellerieTemplateUltra({ id: '4' })).toBe(false);
        expect(validatehotellerieTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validatehotellerieTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderhotellerieTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
