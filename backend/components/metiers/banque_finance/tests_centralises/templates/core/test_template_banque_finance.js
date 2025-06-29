// test_templates_core.js
// Tests avancés pour le module templates core (centralisation tests)
const { renderbanque_financeTemplateUltra, validatebanque_financeTemplateUltra } = require('./template_banque_finance');

describe('Templates Core Central Tests', () => {
    it('should render a valid banque_finance template (nominal)', () => {
        const data = { id: '1', name: 'Cube', meta: { type: 'mesh' }, format: 'obj', i18n: { fr: 'Cube' } };
        const options = { audit: 'ok', accessibility: 'AA', rgpd: 'ok' };
        const result = renderbanque_financeTemplateUltra(data, options);
        expect(result).toContain('Cube');
        expect(result).toContain('Meta:');
        expect(result).toContain('Format: obj');
        expect(result).toContain('I18N:');
        expect(result).toContain('Audit: ok');
        expect(result).toContain('Accessibilité: AA');
        expect(result).toContain('RGPD: ok');
    });

    it('should throw on missing id or name', () => {
        expect(() => renderbanque_financeTemplateUltra({ name: 'Cube' })).toThrow();
        expect(() => renderbanque_financeTemplateUltra({ id: '1' })).toThrow();
        expect(() => renderbanque_financeTemplateUltra({})).toThrow();
    });

    it('should support hooks.beforeRender', () => {
        const data = { id: '2', name: 'Sphere' };
        const options = { hooks: { beforeRender: (output) => output + '\nHOOKED' } };
        const result = renderbanque_financeTemplateUltra(data, options);
        expect(result).toContain('HOOKED');
    });

    it('should validate banque_finance template (nominal, RGPD ok)', () => {
        const data = { id: '3', name: 'Pyramid', rgpd: 'ok' };
        expect(validatebanque_financeTemplateUltra(data)).toBe(true);
    });

    it('should invalidate banque_finance template (missing id/name or RGPD)', () => {
        expect(validatebanque_financeTemplateUltra({ name: 'NoId' })).toBe(false);
        expect(validatebanque_financeTemplateUltra({ id: '4' })).toBe(false);
        expect(validatebanque_financeTemplateUltra({ id: '5', name: 'Bad', rgpd: 'ko' })).toBe(false);
        expect(validatebanque_financeTemplateUltra(null)).toBe(false);
    });

    it('should handle edge cases and advanced options', () => {
        const data = { id: '6', name: 'Edge', meta: {}, format: '', i18n: {} };
        const options = { audit: '', accessibility: '', rgpd: '', hooks: { beforeRender: null } };
        const result = renderbanque_financeTemplateUltra(data, options);
        expect(result).toContain('Edge');
    });
});
