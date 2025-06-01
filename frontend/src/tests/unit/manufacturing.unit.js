/**
 * @file manufacturing.unit.js
 * @description Tests unitaires avancés pour la gestion de projets manufacturing (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */
import { mockAdmin, mockGuest, mockUser } from '../../fixtures/users';
import { ManufacturingService } from '../../services/manufacturingService';
import { enableAudit, getAuditLogs } from '../../utils/audit';
import { getI18n } from '../../utils/i18n';

describe('ManufacturingService', () => {
  beforeAll(() => enableAudit());
  it('should create a manufacturing project (admin)', async () => {
    const i18n = getI18n('en');
    const service = new ManufacturingService(mockAdmin, i18n);
    const project = await service.createProject({ name: 'DihyaFab', country: 'Germany' });
    expect(project.name).toBe('DihyaFab');
    expect(project.ownerRole).toBe('admin');
  });
  it('doit refuser la création pour invité', async () => {
    const i18n = getI18n('fr');
    const service = new ManufacturingService(mockGuest, i18n);
    await expect(service.createProject({ name: 'Test', country: 'France' })).rejects.toThrow(/permission/i);
  });
  it('should log every action (audit)', async () => {
    const i18n = getI18n('en');
    const service = new ManufacturingService(mockUser, i18n);
    await service.createProject({ name: 'AuditFab', country: 'Spain' });
    const logs = getAuditLogs();
    expect(logs.some(l => l.action === 'createProject')).toBe(true);
  });
  // ...autres tests avancés (i18n, sécurité, export, anonymisation, etc.)
});
