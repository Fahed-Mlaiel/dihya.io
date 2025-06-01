// Test: Ecommerce Template
import ecommerceTemplate from './template.js';

describe('ecommerceTemplate', () => {
  it('should return a secure, GDPR, plugin-ready template', () => {
    const doc = ecommerceTemplate({ lang: 'en' });
    expect(doc.title).toBe('Ecommerce');
    expect(doc.security).toBe(true);
    expect(doc.gdpr).toBe(true);
    expect(doc.ci_cd_ready).toBe(true);
  });
});
