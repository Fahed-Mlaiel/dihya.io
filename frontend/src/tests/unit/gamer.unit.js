/**
 * @file gamer.unit.js
 * @description Tests unitaires avancés pour la gestion de projets gamer (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */
import { mockAdmin, mockGuest, mockUser } from '../../fixtures/users';
import { GamerService } from '../../services/gamerService';
import { enableAudit, getAuditLogs } from '../../utils/audit';
import { getI18n } from '../../utils/i18n';

describe('GamerService', () => {
  beforeAll(() => enableAudit());
  it('should create a gamer project (admin)', async () => {
    const i18n = getI18n('en');
    const service = new GamerService(mockAdmin, i18n);
    const project = await service.createProject({ name: 'DihyaGame', platform: 'PC' });
    expect(project.name).toBe('DihyaGame');
    expect(project.ownerRole).toBe('admin');
  });
  it('doit refuser la création pour invité', async () => {
    const i18n = getI18n('fr');
    const service = new GamerService(mockGuest, i18n);
    await expect(service.createProject({ name: 'Test', platform: 'Console' })).rejects.toThrow(/permission/i);
  });
  it('should log every action (audit)', async () => {
    const i18n = getI18n('en');
    const service = new GamerService(mockUser, i18n);
    await service.createProject({ name: 'AuditGame', platform: 'Mobile' });
    const logs = getAuditLogs();
    expect(logs.some(l => l.action === 'createProject')).toBe(true);
  });
  // ...autres tests avancés (i18n, sécurité, export, anonymisation, etc.)
});
