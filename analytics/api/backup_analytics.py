import os
import json
import datetime
from pathlib import Path
from shutil import make_archive, unpack_archive

# Configuration - should be moved to a config file or environment variables
BACKUP_DIR = Path('/path/to/backup/dir')
BACKUP_FORMAT = 'zip'

class BackupManager:
    def __init__(self, backup_dir=BACKUP_DIR):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def _get_timestamp(self):
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    def create_backup(self, data):
        """
        Create a backup of analytics data.
        """
        timestamp = self._get_timestamp()
        backup_file = self.backup_dir / f'analytics_backup_{timestamp}.{BACKUP_FORMAT}'
        with open(backup_file, 'w') as f:
            json.dump(data, f)
        make_archive(str(backup_file), BACKUP_FORMAT, root_dir=str(backup_file.parent), base_dir=backup_file.name)
        os.remove(backup_file)
        return backup_file.with_suffix('')

    def restore_backup(self, backup_file):
        """
        Restore analytics data from a backup.
        """
        if not backup_file.exists():
            raise FileNotFoundError(f'Backup file {backup_file} does not exist.')
        unpack_archive(str(backup_file), extract_dir=str(self.backup_dir), format=BACKUP_FORMAT)

    def list_backups(self):
        """
        List all available backups.
        """
        return list(self.backup_dir.glob(f'*.{BACKUP_FORMAT}'))

    def delete_backup(self, backup_file):
        """
        Delete a specific backup.
        """
        if backup_file.exists():
            backup_file.unlink()
        else:
            raise FileNotFoundError(f'Backup file {backup_file} does not exist.')

# Example usage
if __name__ == '__main__':
    backup_manager = BackupManager()
    analytics_data = {'data': 'Your analytics data here'}

    # Create a backup
    backup_file = backup_manager.create_backup(analytics_data)
    print(f'Backup created: {backup_file}')

    # List backups
    backups = backup_manager.list_backups()
    print(f'Available backups: {backups}')

    # Restore a backup
    backup_manager.restore_backup(backup_file)
    print(f'Backup restored from {backup_file}')

    # Delete a backup
    backup_manager.delete_backup(backup_file)
    print(f'Backup deleted: {backup_file}')