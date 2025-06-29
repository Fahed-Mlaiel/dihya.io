/* global __dirname */
// test_core_helpers.js
// Tests avancés pour le module helpers/core (centralisation tests)
const { TemplatesHelper, renderTemplate, isValidTemplate, mockTemplateContext } = require('../../../../templates/helpers/core/templates_helper');

describe('Templates Helpers Core Central Tests', () => {
    it('should initialize helper with config and audit', () => {
        const helper = new TemplatesHelper();
        const config = { audit: true, rgpd: 'ok' };
        expect(helper.init(config)).toBe(true);
        expect(helper.config).toEqual(config);
        expect(helper.getAuditTrail().length).toBeGreaterThan(0);
    });

    it('should assist with valid operation and audit', () => {
        const helper = new TemplatesHelper();
        helper.init({});
        const result = helper.assist('test', { foo: 'bar' });
        expect(result.success).toBe(true);
        expect(result.operation).toBe('test');
        expect(helper.getAuditTrail().length).toBeGreaterThan(1);
    });

    it('should throw on invalid assist operation', () => {
        const helper = new TemplatesHelper();
        expect(() => helper.assist('', {})).toThrow();
        expect(() => helper.assist(null, {})).toThrow();
    });

    it('should render template with context', () => {
        // Simule un template simple en mémoire (mock fs)
        const fs = require('fs');
        const path = require('path');
        const filePath = path.join(__dirname, 'mock_template.txt');
        fs.writeFileSync(filePath, 'Hello {{ name }}!', 'utf8');
        const result = renderTemplate('mock_template.txt', { name: 'Dihya' });
        expect(result).toContain('Dihya');
        fs.unlinkSync(filePath);
    });

    it('should validate template names', () => {
        expect(isValidTemplate('test.html.j2')).toBe(true);
        expect(isValidTemplate('test.json.j2')).toBe(true);
        expect(isValidTemplate('test.xml')).toBe(true);
        expect(isValidTemplate('test.txt')).toBe(true);
        expect(isValidTemplate('test.exe')).toBe(false);
    });

    it('should provide a valid mock context', () => {
        const ctx = mockTemplateContext();
        expect(ctx.model_name).toBeDefined();
        expect(ctx.status).toBe('OK');
    });
});
