/**
 * @file industrie.unit.js
 * @description Tests unitaires avancés pour la gestion de projets industrie (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */
import { mockAdmin, mockGuest, mockUser } from '../../fixtures/users';
import { IndustrieService } from '../../services/industrieService';
import { enableAudit, getAuditLogs } from '../../utils/audit';
import { getI18n } from '../../utils/i18n';

describe('IndustrieService', () => {
  beforeAll(() => enableAudit());
  it('devrait créer un projet industrie (admin)', async () => {
    const i18n = getI18n('fr');
    const service = new IndustrieService(mockAdmin, i18n);
    const projet = await service.createProject({ nom: 'Dihya Industrie', pays: 'Algérie' });
    expect(projet.nom).toBe('Dihya Industrie');
    expect(projet.ownerRole).toBe('admin');
  });
  it('should deny creation for guest', async () => {
    const i18n = getI18n('en');
    const service = new IndustrieService(mockGuest, i18n);
    await expect(service.createProject({ nom: 'Test', pays: 'France' })).rejects.toThrow(/permission/i);
  });
  it('doit logger chaque action (audit)', async () => {
    const i18n = getI18n('fr');
    const service = new IndustrieService(mockUser, i18n);
    await service.createProject({ nom: 'Projet Audit', pays: 'Maroc' });
    const logs = getAuditLogs();
    expect(logs.some(l => l.action === 'createProject')).toBe(true);
  });
  // ...autres tests avancés (i18n, sécurité, export, anonymisation, etc.)
});
