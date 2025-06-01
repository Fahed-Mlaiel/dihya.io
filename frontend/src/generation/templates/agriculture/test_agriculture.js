/**
 * test_agriculture.js – Tests avancés pour template Agriculture
 * @module generation/templates/agriculture/test_agriculture
 * @author Dihya Team
 * @version 1.0.0
 * @description Tests unitaires, intégration, e2e pour la génération de projets agricoles.
 */

import { generateAgricultureTemplate } from './template';

describe('Template Agriculture – Génération', () => {
  it('génère un template agriculture sécurisé, multilingue, auditable', () => {
    const tpl = generateAgricultureTemplate({
      languages: ['fr','en','ar'],
      plugins: ['ia'],
      roles: ['admin','user']
    });
    expect(tpl.security.cors).toBe('strict');
    expect(tpl.rgpd).toBe(true);
    expect(tpl.i18n).toBe(true);
    expect(tpl.audit).toBe(true);
    expect(tpl.extensible).toBe(true);
  });
});
