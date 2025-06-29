// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderadministration_publiqueTemplateUltra, validateadministration_publiqueTemplateUltra } = require('./template_administration_publique');

describe('Templates Core Central Tests', () => {
    it('should render a valid administration_publique template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderadministration_publiqueTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderadministration_publiqueTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderadministration_publiqueTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderadministration_publiqueTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderadministration_publiqueTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate administration_publique template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validateadministration_publiqueTemplateUltra(data)).toBe(true);
    });

    it('should invalidate administration_publique template (missing id/name or RGPD)', () => {
        expect(validateadministration_publiqueTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validateadministration_publiqueTemplateUltra({ id: '4' })).toBe(false);
        expect(validateadministration_publiqueTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validateadministration_publiqueTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderadministration_publiqueTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
