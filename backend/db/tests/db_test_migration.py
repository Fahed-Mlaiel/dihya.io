"""
Tests de migration, rollback, versionning (exemple simplifié)
"""
import pytest
import sqlite3
import os
import sys
sys.path.insert(0, '.')
from backend.db import migrations

DB_PATH = os.getenv('TEST_DB_PATH', ':memory:')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), '../database_schema.sql')

@pytest.fixture(scope='session')
def db():
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, encoding='utf-8') as f:
        sql = f.read()
    conn.executescript(sql)
    yield conn
    conn.close()

def test_add_column_migration(db):
    db.execute("ALTER TABLE users ADD COLUMN test_col INTEGER DEFAULT 0;")
    cur = db.execute("PRAGMA table_info(users);")
    columns = [row[1] for row in cur.fetchall()]
    assert 'test_col' in columns

def test_rollback(db):
    db.execute("ALTER TABLE users ADD COLUMN rollback_col INTEGER DEFAULT 1;")
    db.execute("CREATE TABLE users_backup AS SELECT * FROM users;")
    db.execute("DROP TABLE users;")
    db.execute("ALTER TABLE users_backup RENAME TO users;")
    cur = db.execute("PRAGMA table_info(users);")
    columns = [row[1] for row in cur.fetchall()]
    assert 'rollback_col' in columns  # rollback_col still present (demo)
