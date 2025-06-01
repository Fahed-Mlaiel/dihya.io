# Exemple de plugin backup Dihya (Python)
from backup_service import BackupPlugin, PLUGINS

class ExampleAuditPlugin(BackupPlugin):
    """
    Plugin d'audit RGPD : logge chaque backup dans un fichier séparé.
    """
    def before_backup(self, data):
        with open('audit_backup.log', 'a') as f:
            f.write(f"[BEFORE] {data}\n")
    def after_backup(self, data):
        with open('audit_backup.log', 'a') as f:
            f.write(f"[AFTER] {data}\n")

PLUGINS.append(ExampleAuditPlugin())
