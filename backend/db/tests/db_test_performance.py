"""
Tests de performance sur index, vues, triggers (SQLite demo)
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

def test_insert_performance(db):
    start = time.time()
    for i in range(1000):
        db.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", (f'user{i}', f'u{i}@ex.com', 'x'))
    db.commit()
    elapsed = time.time() - start
    assert elapsed < 2  # 1000 inserts < 2s
