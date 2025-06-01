/**
 * @file test_backup.js
 * @description Tests unitaires et d’intégration pour le module backup de Dihya Coding.
 * Garantit sécurité, conformité RGPD, auditabilité, robustesse et documentation claire.
 */

import { downloadBackup, listBackups, deleteBackup, clearLocalBackupLogs } from '../backup';

// Mock global fetch et localStorage pour isolation des tests
beforeEach(() => {
  global.fetch = jest.fn();
  localStorage.clear();
});

describe('Backup API – Dihya Coding', () => {
  describe('downloadBackup', () => {
    it('doit lancer une erreur si projectId est invalide', async () => {
      await expect(downloadBackup('')).rejects.toThrow('projectId invalide');
    });

    it('doit télécharger une sauvegarde valide', async () => {
      const fakeBlob = new Blob(['test']);
      fetch.mockResolvedValueOnce({
        ok: true,
        blob: async () => fakeBlob,
      });
      localStorage.setItem('jwt_token', 'token');
      const result = await downloadBackup('project123');
      expect(result).toBeInstanceOf(Blob);
    });

    it('doit logger l’événement de téléchargement', async () => {
      fetch.mockResolvedValueOnce({
        ok: true,
        blob: async () => new Blob(['test']),
      });
      localStorage.setItem('jwt_token', 'token');
      await downloadBackup('project123');
      const logs = JSON.parse(localStorage.getItem('backup_logs'));
      expect(logs[0].action).toBe('download');
      expect(logs[0].id).toBe('project123');
    });
  });

  describe('listBackups', () => {
    it('doit retourner la liste des sauvegardes', async () => {
      const backups = [{ id: 'b1' }, { id: 'b2' }];
      fetch.mockResolvedValueOnce({
        ok: true,
        json: async () => backups,
      });
      localStorage.setItem('jwt_token', 'token');
      const result = await listBackups();
      expect(result).toEqual(backups);
    });

    it('doit lancer une erreur si la récupération échoue', async () => {
      fetch.mockResolvedValueOnce({ ok: false });
      localStorage.setItem('jwt_token', 'token');
      await expect(listBackups()).rejects.toThrow('Erreur lors de la récupération des sauvegardes');
    });
  });

  describe('deleteBackup', () => {
    it('doit lancer une erreur si backupId est invalide', async () => {
      await expect(deleteBackup('')).rejects.toThrow('backupId invalide');
    });

    it('doit supprimer une sauvegarde et logger l’action', async () => {
      fetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({ success: true }),
      });
      localStorage.setItem('jwt_token', 'token');
      const result = await deleteBackup('backup123');
      expect(result.success).toBe(true);
      const logs = JSON.parse(localStorage.getItem('backup_logs'));
      expect(logs[0].action).toBe('delete');
      expect(logs[0].id).toBe('backup123');
    });

    it('doit lancer une erreur si la suppression échoue', async () => {
      fetch.mockResolvedValueOnce({ ok: false });
      localStorage.setItem('jwt_token', 'token');
      await expect(deleteBackup('backup123')).rejects.toThrow('Erreur lors de la suppression de la sauvegarde');
    });
  });

  describe('clearLocalBackupLogs', () => {
    it('doit effacer les logs locaux (RGPD)', () => {
      localStorage.setItem('backup_logs', JSON.stringify([{ action: 'download' }]));
      clearLocalBackupLogs();
      expect(localStorage.getItem('backup_logs')).toBeNull();
    });
  });
});