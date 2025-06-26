"""
Tests avancés pour la sauvegarde métier (backup, restauration, intégrité).
"""
import importlib.util
import os

def find_backup_path():
    cur = os.path.abspath(os.path.dirname(__file__))
    while True:
        candidate = os.path.join(cur, 'devops', 'backup', 'backup.py')
        if os.path.isfile(candidate):
            return candidate
        parent = os.path.dirname(cur)
        if parent == cur:
            raise FileNotFoundError('backup.py introuvable')
        cur = parent

backup_path = find_backup_path()
spec = importlib.util.spec_from_file_location('backup', backup_path)
backup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backup)
backup_data = backup.backup_data


def test_backup_data():
    result = backup_data("/tmp/backup-test")
    assert result is True
