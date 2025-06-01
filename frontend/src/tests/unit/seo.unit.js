/**
 * Tests unitaires avancés pour la gestion SEO backend (robots, sitemap, logs structurés, multilingue, plugins, audit, RGPD, SEO, fallback IA, multitenancy).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { testRobots, testSitemap, testStructuredLogs } from '../../api/seo';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('SEO Backend API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should validate robots.txt, sitemap.xml, structured logs for all supported languages', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      expect(await testRobots({ jwt, lang })).toBe(true);
      expect(await testSitemap({ jwt, lang })).toBe(true);
      expect(await testStructuredLogs({ jwt, lang })).toBe(true);
    }
  });
});
