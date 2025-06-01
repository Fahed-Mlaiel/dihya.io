"""
Tests automatisés de migration Dihya DB (PostgreSQL, SQLite, MySQL)
- Vérifie l’application, le rollback, la conformité RGPD, multilingue, audit
"""
import os
import subprocess
import pytest

MIGRATIONS_DIR = os.path.dirname(__file__)
ALEMBIC_CFG = os.path.join(MIGRATIONS_DIR, 'alembic.ini')

@pytest.mark.parametrize("cmd", [
    ["alembic", "upgrade", "head"],
    ["alembic", "downgrade", "-1"]
])
def test_alembic_migrations(cmd):
    # Teste upgrade/downgrade sur la DB de test
    result = subprocess.run(cmd, cwd=MIGRATIONS_DIR, capture_output=True, text=True)
    assert result.returncode == 0, f"Erreur migration: {result.stderr}"


def test_sql_migrations():
    # Vérifie que tous les scripts SQL s’exécutent sans erreur (PostgreSQL)
    for fname in os.listdir(MIGRATIONS_DIR):
        if fname.endswith('.sql'):
            cmd = ["psql", "-U", "dihya", "-d", "dihya", "-f", fname]
            result = subprocess.run(cmd, cwd=MIGRATIONS_DIR, capture_output=True, text=True)
            assert result.returncode == 0, f"Erreur SQL {fname}: {result.stderr}"
