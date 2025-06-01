/**
 * Tests unitaires avancés pour la gestion de la sécurité (CORS, JWT, WAF, audit, anti-DDOS, plugins, RGPD, SEO, fallback IA, multitenancy, multilingue).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { testAntiDDOS, testAudit, testCORS, testJWT, testWAF } from '../../api/securite';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Sécurité API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should validate CORS, JWT, WAF, audit, anti-DDOS for all supported languages', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      expect(await testCORS({ jwt, lang })).toBe(true);
      expect(await testJWT({ jwt, lang })).toBe(true);
      expect(await testWAF({ jwt, lang })).toBe(true);
      expect(await testAudit({ jwt, lang })).toBe(true);
      expect(await testAntiDDOS({ jwt, lang })).toBe(true);
    }
  });
});
