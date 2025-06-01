/**
 * @file it_devops.unit.js
 * @description Tests unitaires avancés pour la gestion de projets IT/DevOps (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */
import { mockAdmin, mockGuest, mockUser } from '../../fixtures/users';
import { ITDevOpsService } from '../../services/itDevOpsService';
import { enableAudit, getAuditLogs } from '../../utils/audit';
import { getI18n } from '../../utils/i18n';

describe('ITDevOpsService', () => {
  beforeAll(() => enableAudit());
  it('should create an IT/DevOps project (admin)', async () => {
    const i18n = getI18n('en');
    const service = new ITDevOpsService(mockAdmin, i18n);
    const project = await service.createProject({ name: 'DihyaOps', stack: 'K8s' });
    expect(project.name).toBe('DihyaOps');
    expect(project.ownerRole).toBe('admin');
  });
  it('doit refuser la création pour invité', async () => {
    const i18n = getI18n('fr');
    const service = new ITDevOpsService(mockGuest, i18n);
    await expect(service.createProject({ name: 'Test', stack: 'Docker' })).rejects.toThrow(/permission/i);
  });
  it('should log every action (audit)', async () => {
    const i18n = getI18n('en');
    const service = new ITDevOpsService(mockUser, i18n);
    await service.createProject({ name: 'AuditOps', stack: 'Linux' });
    const logs = getAuditLogs();
    expect(logs.some(l => l.action === 'createProject')).toBe(true);
  });
  // ...autres tests avancés (i18n, sécurité, export, anonymisation, etc.)
});
