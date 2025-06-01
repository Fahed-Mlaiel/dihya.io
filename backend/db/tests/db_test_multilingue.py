"""
Tests d'internationalisation des données (langues supportées, valeurs par défaut)
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

def test_default_lang_fr(db):
    db.execute("INSERT INTO users (username, email, password_hash) VALUES ('langtest', 'lang@ex.com', 'x')")
    cur = db.execute("SELECT lang FROM users WHERE username='langtest'")
    assert cur.fetchone()[0] == 'fr'

def test_supported_languages(db):
    for lang in ['fr', 'en', 'ar', 'tzm']:
        db.execute("INSERT INTO users (username, email, password_hash, lang) VALUES (?, ?, ?, ?)", (f'user_{lang}', f'{lang}@ex.com', 'x', lang))
        cur = db.execute("SELECT lang FROM users WHERE username=?", (f'user_{lang}',))
        assert cur.fetchone()[0] == lang
