// Test: Hotellerie Template
import hotellerieTemplate from './template.js';

describe('hotellerieTemplate', () => {
  it('should return a secure, GDPR, plugin-ready template', () => {
    const doc = hotellerieTemplate({ lang: 'en' });
    expect(doc.title).toBe('Hospitality');
    expect(doc.security).toBe(true);
    expect(doc.gdpr).toBe(true);
    expect(doc.ci_cd_ready).toBe(true);
  });
});
