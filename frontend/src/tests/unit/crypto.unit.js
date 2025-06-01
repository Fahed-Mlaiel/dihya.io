/**
 * @file crypto.unit.js
 * @description Tests unitaires avancés pour la gestion de projets crypto (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */
import { mockAdmin, mockGuest, mockUser } from '../../fixtures/users';
import { CryptoService } from '../../services/cryptoService';
import { enableAudit, getAuditLogs } from '../../utils/audit';
import { getI18n } from '../../utils/i18n';

describe('CryptoService', () => {
  beforeAll(() => enableAudit());
  it('should create a crypto project (admin)', async () => {
    const i18n = getI18n('en');
    const service = new CryptoService(mockAdmin, i18n);
    const project = await service.createProject({ name: 'DihyaCoin', chain: 'Ethereum' });
    expect(project.name).toBe('DihyaCoin');
    expect(project.ownerRole).toBe('admin');
  });
  it('doit refuser la création pour invité', async () => {
    const i18n = getI18n('fr');
    const service = new CryptoService(mockGuest, i18n);
    await expect(service.createProject({ name: 'Test', chain: 'Polygon' })).rejects.toThrow(/permission/i);
  });
  it('should log every action (audit)', async () => {
    const i18n = getI18n('en');
    const service = new CryptoService(mockUser, i18n);
    await service.createProject({ name: 'AuditCoin', chain: 'Solana' });
    const logs = getAuditLogs();
    expect(logs.some(l => l.action === 'createProject')).toBe(true);
  });
  // ...autres tests avancés (i18n, sécurité, export, anonymisation, etc.)
});
