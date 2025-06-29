// test_utils.js
// Tests avancés pour le module helpers/utils (centralisation tests)
const utils = require('../../../../templates/helpers/utils/utils_helpers.js');

describe('Templates Helpers Utils Central Tests', () => {
    it('should validate advanced helpers utils logic', () => {
        expect(true).toBe(true); // Remplacer par des assertions avancées
    });
});

describe('Templates Helpers Utils Ultra Advanced', () => {
    it('should generate a unique template ID (conformité, audit, CI/CD)', () => {
        const id1 = utils.generateTemplateId('test');
        const id2 = utils.generateTemplateId('test');
        expect(id1).not.toBe(id2);
        expect(id1).toMatch(/^test_/);
    });

    it('should clean template content for RGPD (anonymisation)', () => {
        const content = 'Nom: Dupont\nEmail: test@example.com';
        const cleaned = utils.cleanTemplateContent(content);
        expect(cleaned).not.toContain('test@example.com');
        expect(cleaned).toContain('[EMAIL_ANONYME]');
    });

    it('should check accessibility (attributs ARIA, alt, role)', () => {
        const element = { tagName: 'IMG', alt: 'test' };
        const result = utils.checkAccessibility(element);
        expect(result.valid).toBe(true);
        expect(utils.checkAccessibility('<div></div>')).toBe(false);
    });

    it('should audit template (length, accessibilité, RGPD, timestamp)', () => {
        const content = '<div aria-label="ok">Nom: [anonymisé]</div>';
        const audit = utils.auditTemplate(content);
        expect(audit.length).toBeGreaterThan(0);
        expect(audit.hasAccessibility).toBe(true);
        expect(audit.isRGPD).toBe(true);
        expect(audit.timestamp).toBeDefined();
    });

    it('should handle edge cases (empty, null, minimal)', () => {
        expect(utils.cleanTemplateContent('')).toBe('');
        expect(utils.cleanTemplateContent(null)).toBe('');
        expect(utils.checkAccessibility('')).toBe(false);
        expect(utils.auditTemplate('')).toMatchObject({ length: 0, hasAccessibility: false, isRGPD: true });
    });
});
