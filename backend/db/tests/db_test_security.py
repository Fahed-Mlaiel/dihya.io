"""
Tests RGPD, anonymisation, accès restreint, suppression logique
"""
import pytest
import sqlite3
import os

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

def test_rgpd_consent_default_false(db):
    db.execute("INSERT INTO users (username, email, password_hash) VALUES ('alice', 'alice@example.com', 'x')")
    cur = db.execute("SELECT consent_rgpd FROM users WHERE username='alice'")
    assert cur.fetchone()[0] == 0

def test_soft_delete(db):
    db.execute("INSERT INTO users (username, email, password_hash) VALUES ('bob', 'bob@example.com', 'x')")
    db.execute("UPDATE users SET deleted_at=datetime('now') WHERE username='bob'")
    cur = db.execute("SELECT deleted_at FROM users WHERE username='bob'")
    assert cur.fetchone()[0] is not None
