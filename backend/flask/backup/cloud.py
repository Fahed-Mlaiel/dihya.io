# backup/cloud.py — Sauvegarde cloud (exemple AWS S3, extensible)

"""
Module de sauvegarde cloud pour Dihya Coding.
Permet de sauvegarder des fichiers/dossiers critiques sur un bucket S3 (ou autre cloud), avec journalisation, gestion d’erreurs et conformité RGPD.

Bonnes pratiques :
- Ne jamais inclure de secrets ou données personnelles non chiffrées.
- Protéger les credentials via variables d’environnement.
- Logger chaque opération de backup/restauration.
- Gérer les erreurs réseau, quotas, permissions, etc.
- Prévoir la restauration automatisée.

Exemple d’utilisation :
    from backup.cloud import backup_to_s3
    backup_to_s3('/chemin/vers/fichier.txt', 'mon-bucket', 'backup/')
"""

import os
from datetime import datetime
import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'eu-west-1')

def backup_to_s3(src_path, bucket, prefix=''):
    """
    Sauvegarde un fichier sur un bucket S3.
    """
    if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
        print("Clés AWS manquantes.")
        return False
    if not os.path.exists(src_path):
        print(f"Source introuvable : {src_path}")
        return False
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)
    base_name = os.path.basename(src_path)
    timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    key = f"{prefix}{base_name}_{timestamp}"
    try:
        s3.upload_file(src_path, bucket, key)
        print(f"Backup S3 réussi : s3://{bucket}/{key}")
        return True
    except (BotoCoreError, NoCredentialsError, Exception) as e:
        print(f"Erreur backup S3 : {e}")
        return False
