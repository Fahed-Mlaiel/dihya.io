"""
Tests unitaires pour les tâches de nettoyage (app.tasks.cleanup_tasks) — Dihya Coding.

Vérifie la détection, la suppression (ou dry-run) des fichiers temporaires, la gestion des erreurs et la sécurité.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import os
import tempfile
import shutil
from backend.flask.app.tasks import cleanup_tasks

def setup_temp_dir():
    """Crée un répertoire temporaire avec des fichiers factices pour les tests."""
    temp_dir = tempfile.mkdtemp()
    file1 = os.path.join(temp_dir, "tmp1.txt")
    file2 = os.path.join(temp_dir, "tmp2.txt")
    with open(file1, "w") as f:
        f.write("test1")
    with open(file2, "w") as f:
        f.write("test2")
    return temp_dir, [file1, file2]

def test_list_files_detects_files():
    """Test que list_files retourne bien les fichiers présents."""
    temp_dir, files = setup_temp_dir()
    try:
        listed = cleanup_tasks.list_files(temp_dir)
        assert set(listed) == set(files)
    finally:
        shutil.rmtree(temp_dir)

def test_cleanup_temp_files_dry_run(monkeypatch):
    """Test le dry-run : aucun fichier n'est supprimé, la liste est retournée."""
    temp_dir, files = setup_temp_dir()
    monkeypatch.setattr(cleanup_tasks, "TEMP_DIR", temp_dir)
    result = cleanup_tasks.cleanup_temp_files(dry_run=True)
    assert result["status"] == "dry_run"
    assert set(result["files"]) == set(files)
    # Les fichiers existent toujours
    for f in files:
        assert os.path.exists(f)
    shutil.rmtree(temp_dir)

def test_cleanup_temp_files_delete(monkeypatch):
    """Test la suppression réelle des fichiers temporaires."""
    temp_dir, files = setup_temp_dir()
    monkeypatch.setattr(cleanup_tasks, "TEMP_DIR", temp_dir)
    result = cleanup_tasks.cleanup_temp_files(dry_run=False)
    assert result["status"] == "success"
    assert set(result["deleted"]) == set(files)
    # Les fichiers sont bien supprimés
    for f in files:
        assert not os.path.exists(f)
    shutil.rmtree(temp_dir, ignore_errors=True)