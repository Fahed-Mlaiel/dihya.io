// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderservices_personneTemplateUltra, validateservices_personneTemplateUltra } = require('./template_services_personne');

describe('Templates Core Central Tests', () => {
    it('should render a valid services_personne template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderservices_personneTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderservices_personneTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderservices_personneTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderservices_personneTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderservices_personneTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate services_personne template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validateservices_personneTemplateUltra(data)).toBe(true);
    });

    it('should invalidate services_personne template (missing id/name or RGPD)', () => {
        expect(validateservices_personneTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validateservices_personneTemplateUltra({ id: '4' })).toBe(false);
        expect(validateservices_personneTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validateservices_personneTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderservices_personneTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
