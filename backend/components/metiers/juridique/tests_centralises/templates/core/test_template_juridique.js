// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderjuridiqueTemplateUltra, validatejuridiqueTemplateUltra } = require('./template_juridique');

describe('Templates Core Central Tests', () => {
    it('should render a valid juridique template (nominal)', () => {
        const data = { id: '1', name: 'Dossier', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Dossier' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderjuridiqueTemplateUltra(data, options);
        expect(result).toContain('Dossier');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderjuridiqueTemplateUltra({ name: 'Dossier' })).toThrow();
        expect(() => renderjuridiqueTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderjuridiqueTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderjuridiqueTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate juridique template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validatejuridiqueTemplateUltra(data)).toBe(true);
    });

    it('should invalidate juridique template (missing id/name or RGPD)', () => {
        expect(validatejuridiqueTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validatejuridiqueTemplateUltra({ id: '4' })).toBe(false);
        expect(validatejuridiqueTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validatejuridiqueTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderjuridiqueTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
