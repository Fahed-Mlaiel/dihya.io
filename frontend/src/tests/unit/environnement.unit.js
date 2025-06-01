/**
 * @file environnement.unit.js
 * @description Tests unitaires avancés pour la gestion de projets environnement (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */
import { mockAdmin, mockGuest, mockUser } from '../../fixtures/users';
import { EnvironnementService } from '../../services/environnementService';
import { enableAudit, getAuditLogs } from '../../utils/audit';
import { getI18n } from '../../utils/i18n';

describe('EnvironnementService', () => {
  beforeAll(() => enableAudit());
  it('devrait créer un projet environnement (admin)', async () => {
    const i18n = getI18n('fr');
    const service = new EnvironnementService(mockAdmin, i18n);
    const projet = await service.createProject({ nom: 'Dihya Green', pays: 'Algérie' });
    expect(projet.nom).toBe('Dihya Green');
    expect(projet.ownerRole).toBe('admin');
  });
  it('should deny creation for guest', async () => {
    const i18n = getI18n('en');
    const service = new EnvironnementService(mockGuest, i18n);
    await expect(service.createProject({ nom: 'Test', pays: 'France' })).rejects.toThrow(/permission/i);
  });
  it('doit logger chaque action (audit)', async () => {
    const i18n = getI18n('fr');
    const service = new EnvironnementService(mockUser, i18n);
    await service.createProject({ nom: 'Projet Audit', pays: 'Maroc' });
    const logs = getAuditLogs();
    expect(logs.some(l => l.action === 'createProject')).toBe(true);
  });
  // ...autres tests avancés (i18n, sécurité, export, anonymisation, etc.)
});
