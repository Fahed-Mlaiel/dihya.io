// Test: Gamer Template
import gamerTemplate from './template.js';

describe('gamerTemplate', () => {
  it('should return a secure, GDPR, plugin-ready template', () => {
    const doc = gamerTemplate({ lang: 'en' });
    expect(doc.title).toBe('Game');
    expect(doc.security).toBe(true);
    expect(doc.gdpr).toBe(true);
    expect(doc.ci_cd_ready).toBe(true);
  });
});
