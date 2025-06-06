# index.test.py – Test d’intégration du point d’entrée JS plugins guides/core
import subprocess

def test_index_js_entrypoint():
    result = subprocess.run(['node', 'index.js'], cwd='backend/components/metiers/threed/guides/core/plugins', capture_output=True)
    assert result.returncode == 0
