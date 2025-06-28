const assert = require('assert');
const { renderTemplate, extractVariables, hasRequiredVariables, cleanTemplate, isValidTemplate, mockTemplateContext, TemplatesHelper } = require('../../../../templates/helpers/core/templates_helper');

// Import basique ajouté automatiquement
// test_templates_helpers.js
// Tests avancés pour helpers du module templates (centralisation tests)
describe('Templates Templates Helpers Central Tests', () => {
    it('renderTemplate remplace les variables', () => {
        const tpl = 'Bonjour {{name}}, statut: {{status}}';
        const res = renderTemplate(tpl, { name: 'Dihya', status: 'OK' });
        expect(res).toBe('Bonjour Dihya, statut: OK');
    });
    it('extractVariables extrait toutes les variables', () => {
        const tpl = 'A={{a}}, B={{b}}';
        expect(extractVariables(tpl)).toEqual(['a', 'b']);
    });
    it('hasRequiredVariables détecte les variables manquantes', () => {
        const tpl = 'A={{a}}, B={{b}}';
        expect(hasRequiredVariables(tpl, ['a', 'b'])).toBe(true);
        expect(hasRequiredVariables(tpl, ['a', 'b', 'c'])).toBe(false);
    });
    it('cleanTemplate supprime les variables non remplacées', () => {
        const tpl = 'Bonjour {{name}}, statut: {{status}}';
        expect(cleanTemplate(tpl)).toBe('Bonjour , statut: ');
    });
    it('isValidTemplate reconnaît les extensions valides', () => {
        expect(isValidTemplate('x.html')).toBe(true);
        expect(isValidTemplate('x.txt')).toBe(true);
        expect(isValidTemplate('x.exe')).toBe(false);
    });
    it('mockTemplateContext retourne un contexte simulé', () => {
        const ctx = mockTemplateContext();
        expect(ctx).toHaveProperty('model_name');
        expect(ctx).toHaveProperty('status');
        expect(ctx).toHaveProperty('date');
    });
    it('TemplatesHelper auditTrail fonctionne', () => {
        const helper = new TemplatesHelper();
        helper.init({ foo: 'bar' });
        helper.assist('test', { a: 1 });
        const trail = helper.getAuditTrail();
        expect(Array.isArray(trail)).toBe(true);
        expect(trail.length).toBeGreaterThanOrEqual(2);
    });
});
