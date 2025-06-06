# index.test.py – Test d’intégration du point d’entrée JS fixtures
import subprocess

def test_index_js_entrypoint():
    result = subprocess.run(['node', 'index.js'], cwd='backend/components/metiers/threed/guides/core/fixtures', capture_output=True)
    assert result.returncode == 0
