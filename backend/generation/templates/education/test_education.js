// Test: Education Template
import educationTemplate from './template.js';

describe('educationTemplate', () => {
  it('should return a secure, GDPR, plugin-ready template', () => {
    const doc = educationTemplate({ lang: 'en' });
    expect(doc.title).toBe('Education');
    expect(doc.security).toBe(true);
    expect(doc.gdpr).toBe(true);
    expect(doc.ci_cd_ready).toBe(true);
  });
});
