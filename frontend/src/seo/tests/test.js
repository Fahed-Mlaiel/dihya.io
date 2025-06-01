// test.js - Test unitaire et d'intégration pour SEO (Node.js)
/**
 * @file Test complet SEO backend (robots, sitemap, logs structurés)
 * @author Dihya
 * @version 1.0
 */
const { generateSitemap, logSEOEvent } = require('../seo');
const assert = require('assert');

describe('SEO Backend', () => {
  it('should generate a valid sitemap', () => {
    const sitemap = generateSitemap(['/', '/about']);
    assert.ok(sitemap.includes('<urlset'));
  });

  it('should log SEO events', () => {
    assert.strictEqual(logSEOEvent('visit', '/'), 'logged');
  });
});
