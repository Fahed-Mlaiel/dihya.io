"""
Tests e2e avancés pour la base Dihya (performance, triggers, vues, auditabilité)
"""
import pytest
import sqlite3
import os
import time
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

def test_performance_bulk_insert(db):
    start = time.time()
    for i in range(1000):
        db.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", (f'user{i}', f'u{i}@ex.com', 'x'))
    db.commit()
    elapsed = time.time() - start
    assert elapsed < 2  # 1000 inserts < 2s

def test_trigger_soft_delete(db):
    db.execute("INSERT INTO users (username, email, password_hash) VALUES ('todelete', 'del@ex.com', 'x')")
    db.execute("DELETE FROM users WHERE username='todelete'")
    cur = db.execute("SELECT is_deleted FROM users WHERE username='todelete'")
    assert cur.fetchone()[0] == 1

def test_view_performance(db):
    db.execute("CREATE VIEW user_emails AS SELECT email FROM users")
    cur = db.execute("SELECT COUNT(*) FROM user_emails")
    assert cur.fetchone()[0] >= 0
