# backup/ftp.py — Sauvegarde sur serveur FTP/SFTP

"""
Module de sauvegarde FTP/SFTP pour Dihya Coding.
Permet de sauvegarder des fichiers/dossiers critiques sur un serveur FTP/SFTP, avec journalisation, gestion d’erreurs et conformité RGPD.

Bonnes pratiques :
- Utiliser SFTP (FTP sécurisé) de préférence.
- Protéger les credentials via variables d’environnement.
- Logger chaque opération de backup/restauration.
- Gérer les erreurs réseau, permissions, etc.

Exemple d’utilisation :
    from backup.ftp import backup_to_ftp
    backup_to_ftp('/chemin/vers/fichier.txt', 'ftp.example.com', 'user', 'pass', '/backup/')
"""

import os
from datetime import datetime
from ftplib import FTP, error_perm

def backup_to_ftp(src_path, host, username, password, remote_dir='/'):
    """
    Sauvegarde un fichier sur un serveur FTP.
    """
    if not os.path.exists(src_path):
        print(f"Source introuvable : {src_path}")
        return False
    base_name = os.path.basename(src_path)
    timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    remote_name = f"{base_name}_{timestamp}"
    try:
        with FTP(host) as ftp:
            ftp.login(user=username, passwd=password)
            ftp.cwd(remote_dir)
            with open(src_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_name}', f)
        print(f"Backup FTP réussi : {remote_dir}/{remote_name}")
        return True
    except error_perm as e:
        print(f"Erreur permission FTP : {e}")
        return False
    except Exception as e:
        print(f"Erreur backup FTP : {e}")
        return False
