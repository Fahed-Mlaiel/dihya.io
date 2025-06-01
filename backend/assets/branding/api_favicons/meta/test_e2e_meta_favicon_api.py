# Dihya API Favicon – Test e2e d’export et d’intégration

import subprocess
import json

def test_export_json():
    result = subprocess.run([
        'python', 'export_meta_favicon_api.py', '--export', 'json'
    ], capture_output=True, text=True, check=True)
    meta = json.loads(result.stdout)
    assert meta["name"] == "Dihya API Favicon"
    assert meta["rgpd"]["conformite"] is True
    assert meta["accessibility"]["contrast"] == "AAA"

def test_plugin_audit():
    result = subprocess.run([
        'python', 'plugin_audit_meta_favicon.py'
    ], capture_output=True, text=True, check=True)
    assert "OK" in result.stdout
