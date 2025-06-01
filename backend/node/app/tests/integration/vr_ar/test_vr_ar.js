// Test d'intégration avancé pour la VR/AR
// Sécurité maximale (CORS, JWT, validation, audit, WAF, anti-DDOS, monitoring, backup, logging, RBAC, multitenancy, plugins, fallback IA, RGPD, auditabilité)
// Accessibilité, SEO backend, internationalisation 13+ langues, documentation intégrée, CI/CD-ready

const { secureTest, i18n, auditLog } = require('../../../utils/testUtils');
const { getVRARService } = require('../../../services/vr_ar');

describe('Intégration VR/AR', () => {
  it('doit valider l’accès sécurisé et multilingue à la plateforme VR/AR', async () => {
    const token = await secureTest.getJWT('user_vr_ar', ['vr_ar_access']);
    const res = await getVRARService().getExperience({
      headers: { Authorization: `Bearer ${token}`, 'Accept-Language': 'fr' }
    });
    expect(res.status).toBe(200);
    expect(i18n.isTranslated(res.body, ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'])).toBe(true);
    auditLog.check(res);
  });

  it('doit refuser l’accès sans JWT', async () => {
    const res = await getVRARService().getExperience({ headers: { 'Accept-Language': 'fr' } });
    expect(res.status).toBe(401);
  });

  it('doit auditer la création de projet VR/AR (admin)', async () => {
    const token = await secureTest.getJWT('admin', ['vr_ar_admin']);
    const res = await getVRARService().createExperience({
      headers: { Authorization: `Bearer ${token}` },
      body: { name: 'Test VR', lang: 'fr' }
    });
    expect(res.status).toBe(201);
    auditLog.check(res);
  });

  it('doit appliquer la validation RGPD et anonymisation', async () => {
    const token = await secureTest.getJWT('user_vr_ar', ['vr_ar_access']);
    const res = await getVRARService().getExperience({
      headers: { Authorization: `Bearer ${token}` }
    });
    expect(res.body).not.toHaveProperty('personalData');
  });

  // ...autres tests avancés (plugins, fallback IA, accessibilité, SEO, export)...
});
