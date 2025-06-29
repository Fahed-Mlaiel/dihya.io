// test_templates_validator.js – Tests avancés helpers/validators (JS)
const path = require('path');
const fs = require('fs');
const { isValidTemplateFile, validateTemplateContent } = require('../../../../templates/helpers/validators/templates_validator');

describe('Templates Helpers Validators Ultra Advanced', () => {
    it('should validate template file existence and extension', () => {
        const filePath = path.join(__dirname, 'mock_template.html.j2');
        fs.writeFileSync(filePath, '<div>{{ var }}</div>', 'utf8');
        expect(isValidTemplateFile(filePath)).toBe(true);
        fs.unlinkSync(filePath);
        expect(isValidTemplateFile(filePath)).toBe(false);
        expect(isValidTemplateFile('invalid.exe')).toBe(false);
    });

    it('should validate template content (Jinja2, HTML, JSON, edge cases)', () => {
        expect(validateTemplateContent('<div>{{ var }}</div>')).toBe(true);
        expect(validateTemplateContent('{ "a": 1 }')).toBe(true);
        expect(validateTemplateContent('no tags')).toBe(false);
        expect(validateTemplateContent('')).toBe(false);
    });

    it('should handle edge cases and CI/CD compliance', () => {
        expect(validateTemplateContent('{{}}')).toBe(true);
        expect(validateTemplateContent('<>')).toBe(true);
        expect(validateTemplateContent('{}')).toBe(true);
    });
});
