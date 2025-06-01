// Test: Construction Template
import constructionTemplate from './template.js';

describe('constructionTemplate', () => {
  it('should return a secure, GDPR, plugin-ready template', () => {
    const doc = constructionTemplate({ lang: 'en' });
    expect(doc.title).toBe('Construction');
    expect(doc.security).toBe(true);
    expect(doc.gdpr).toBe(true);
    expect(doc.ci_cd_ready).toBe(true);
  });
});
