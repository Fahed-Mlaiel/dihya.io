/**
 * @file test_infra.js
 * @description Tests unitaires et d’intégration pour l’infrastructure Dihya Coding (DWeb, IPFS, sauvegarde, restauration, RGPD, auditabilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests valident la conformité, la sécurité, la robustesse et la traçabilité des modules infra.
 */

import { saveToDWeb, restoreFromDWeb, clearLocalDWebServiceLogs } from '../dweb/dwebService';
import { saveToIPFS, restoreFromIPFS, clearLocalIPFSServiceLogs } from '../ipfs/ipfsService';

describe('Infra Dihya Coding – DWeb', () => {
  beforeEach(() => {
    window.localStorage.clear();
    window.localStorage.setItem('dweb_service_feature_consent', '1');
  });

  test('sauvegarde DWeb avec consentement', async () => {
    const result = await saveToDWeb({ projectId: 'proj_test', data: { foo: 'bar' } });
    expect(result.success).toBe(true);
    expect(result.backupId).toMatch(/^backup_proj_test_/);
  });

  test('restauration DWeb avec consentement', async () => {
    const backupId = 'backup_proj_test_' + Date.now().toString(36);
    const result = await restoreFromDWeb({ backupId });
    expect(result.data).toBeDefined();
    expect(result.data.restored).toBe(true);
    expect(result.data.backupId).toBe(backupId);
  });

  test('droit à l’oubli DWeb', () => {
    window.localStorage.setItem('dweb_service_logs', JSON.stringify([{ action: 'test', data: {} }]));
    clearLocalDWebServiceLogs();
    expect(window.localStorage.getItem('dweb_service_logs')).toBeNull();
  });

  test('refus sans consentement DWeb', async () => {
    window.localStorage.removeItem('dweb_service_feature_consent');
    await expect(saveToDWeb({ projectId: 'proj_test', data: {} }))
      .rejects.toThrow(/Consentement requis/);
  });
});

describe('Infra Dihya Coding – IPFS', () => {
  beforeEach(() => {
    window.localStorage.clear();
    window.localStorage.setItem('ipfs_service_feature_consent', '1');
  });

  test('sauvegarde IPFS avec consentement', async () => {
    const result = await saveToIPFS({ projectId: 'proj_test', data: { foo: 'bar' } });
    expect(result.success).toBe(true);
    expect(result.cid).toMatch(/^cid_/);
  });

  test('restauration IPFS avec consentement', async () => {
    const cid = 'cid_' + btoa('proj_test{}').slice(0, 16) + Date.now().toString(36);
    const result = await restoreFromIPFS({ cid });
    expect(result.data).toBeDefined();
    expect(result.data.restored).toBe(true);
    expect(result.data.cid).toBe(cid);
  });

  test('droit à l’oubli IPFS', () => {
    window.localStorage.setItem('ipfs_service_logs', JSON.stringify([{ action: 'test', data: {} }]));
    clearLocalIPFSServiceLogs();
    expect(window.localStorage.getItem('ipfs_service_logs')).toBeNull();
  });

  test('refus sans consentement IPFS', async () => {
    window.localStorage.removeItem('ipfs_service_feature_consent');
    await expect(saveToIPFS({ projectId: 'proj_test', data: {} }))
      .rejects.toThrow(/Consentement requis/);
  });
});