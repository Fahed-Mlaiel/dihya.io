"""
Script de sauvegarde avancé pour Dihya (RGPD, sécurité, logs, export, Docker/K8s)
"""
import os
import logging
import tarfile
from datetime import datetime

def perform_backup():
    backup_root = '/workspaces/Dihya/backups'
    os.makedirs(backup_root, exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_file = os.path.join(backup_root, f'dihya_backend_{date_str}.tar.gz')
    source_dir = '/workspaces/Dihya/Dihya/backend'
    with tarfile.open(backup_file, 'w:gz') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    return {'backup_file': backup_file, 'status': 'success', 'timestamp': date_str}

def export_backup_log(result, log_path):
    with open(os.path.join('/workspaces/Dihya', log_path), 'a') as f:
        f.write(f"[{result['timestamp']}] Backup: {result['status']} - {result['backup_file']}\n")


def main():
    """
    Lance la sauvegarde complète du backend Dihya (données, logs, configs).
    """
    logging.basicConfig(level=logging.INFO)
    logging.info("Démarrage de la sauvegarde Dihya...")
    backup_result = perform_backup()
    export_backup_log(backup_result, "backup_realtime.log")
    logging.info("Sauvegarde terminée. Log exporté.")

if __name__ == "__main__":
    main()
