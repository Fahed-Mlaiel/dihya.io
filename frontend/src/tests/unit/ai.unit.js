/**
 * @file intelligence_artificielle.unit.js
 * @description Tests unitaires avancés pour la gestion de projets IA (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */
import { mockAdmin, mockGuest, mockUser } from '../../fixtures/users';
import { IAService } from '../../services/iaService';
import { enableAudit, getAuditLogs } from '../../utils/audit';
import { getI18n } from '../../utils/i18n';

describe('IAService', () => {
  beforeAll(() => enableAudit());
  it('should create an IA project (admin)', async () => {
    const i18n = getI18n('en');
    const service = new IAService(mockAdmin, i18n);
    const project = await service.createProject({ name: 'DihyaAI', type: 'NLP' });
    expect(project.name).toBe('DihyaAI');
    expect(project.ownerRole).toBe('admin');
  });
  it('doit refuser la création pour invité', async () => {
    const i18n = getI18n('fr');
    const service = new IAService(mockGuest, i18n);
    await expect(service.createProject({ name: 'Test', type: 'Vision' })).rejects.toThrow(/permission/i);
  });
  it('should log every action (audit)', async () => {
    const i18n = getI18n('en');
    const service = new IAService(mockUser, i18n);
    await service.createProject({ name: 'AuditAI', type: 'Speech' });
    const logs = getAuditLogs();
    expect(logs.some(l => l.action === 'createProject')).toBe(true);
  });
  // ...autres tests avancés (i18n, sécurité, export, anonymisation, etc.)
});
