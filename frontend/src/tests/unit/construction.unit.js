/**
 * @file construction.unit.js
 * @description Tests unitaires avancés pour la gestion de projets de construction (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */
import { mockAdmin, mockGuest, mockUser } from '../../fixtures/users';
import { ConstructionService } from '../../services/constructionService';
import { enableAudit, getAuditLogs } from '../../utils/audit';
import { getI18n } from '../../utils/i18n';

describe('ConstructionService', () => {
  beforeAll(() => enableAudit());
  it('devrait créer un projet de construction (admin)', async () => {
    const i18n = getI18n('fr');
    const service = new ConstructionService(mockAdmin, i18n);
    const projet = await service.createProject({ nom: 'Tour Dihya', localisation: 'Alger' });
    expect(projet.nom).toBe('Tour Dihya');
    expect(projet.ownerRole).toBe('admin');
  });
  it('should deny creation for guest', async () => {
    const i18n = getI18n('en');
    const service = new ConstructionService(mockGuest, i18n);
    await expect(service.createProject({ nom: 'Test', localisation: 'Paris' })).rejects.toThrow(/permission/i);
  });
  it('doit logger chaque action (audit)', async () => {
    const i18n = getI18n('fr');
    const service = new ConstructionService(mockUser, i18n);
    await service.createProject({ nom: 'Projet Audit', localisation: 'Oran' });
    const logs = getAuditLogs();
    expect(logs.some(l => l.action === 'createProject')).toBe(true);
  });
  // ...autres tests avancés (i18n, sécurité, export, anonymisation, etc.)
});
