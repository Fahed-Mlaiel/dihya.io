// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderartsTemplateUltra, validateartsTemplateUltra } = require('./template_arts');

describe('Templates Core Central Tests', () => {
    it('should render a valid arts template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderartsTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderartsTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderartsTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderartsTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderartsTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate arts template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validateartsTemplateUltra(data)).toBe(true);
    });

    it('should invalidate arts template (missing id/name or RGPD)', () => {
        expect(validateartsTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validateartsTemplateUltra({ id: '4' })).toBe(false);
        expect(validateartsTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validateartsTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderartsTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
