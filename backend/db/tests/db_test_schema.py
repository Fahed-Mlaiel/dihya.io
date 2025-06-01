"""
Tests de validation du schéma SQL (PostgreSQL, MySQL, SQLite)
"""
import pytest
import os
import sqlite3
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

def test_users_table_exists(db):
    cur = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    assert cur.fetchone() is not None

def test_audit_logs_table_exists(db):
    cur = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='audit_logs';")
    assert cur.fetchone() is not None

def test_users_table_columns(db):
    cur = db.execute("PRAGMA table_info(users);")
    columns = [row[1] for row in cur.fetchall()]
    for col in ['id', 'username', 'email', 'password_hash', 'role', 'lang', 'is_active', 'consent_rgpd']:
        assert col in columns
