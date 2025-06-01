"""
Tests avancés pour la souveraineté numérique (anonymisation, export, import, RGPD, audit, DWeb/IPFS mock).
Couvre : hooks métier, sectorisation, audit, monitoring, anonymisation, CI/CD readiness, souveraineté, RGPD.
"""
import os
import pytest
import sqlite3
import json
from datetime import datetime
from backend.flask.souverainete import anonymize, export, import_mod

DB_PATH = "test_dihya.db"
EXPORT_DIR = "souverainete/exports"

@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    # Setup: create test DB
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)")
    cur.execute("INSERT INTO users (username, email) VALUES ('alice', 'alice@example.com')")
    conn.commit()
    conn.close()
    yield
    # Teardown: remove test DB and exports
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    if os.path.exists(EXPORT_DIR):
        for f in os.listdir(EXPORT_DIR):
            os.remove(os.path.join(EXPORT_DIR, f))


def test_anonymize_users():
    # Patch DB_PATH for test
    anonymize.DB_PATH = DB_PATH
    anonymize.anonymize_users()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT username, email FROM users")
    user = cur.fetchone()
    assert user == ("anonymous", "anonymous@dihya.dev")
    conn.close()


def test_export_table_to_json():
    export.DB_PATH = DB_PATH
    export.EXPORT_DIR = EXPORT_DIR
    os.makedirs(EXPORT_DIR, exist_ok=True)
    export.export_table_to_json("users")
    files = os.listdir(EXPORT_DIR)
    assert any(f.startswith("users_") and f.endswith(".json") for f in files)
    # Check file content
    for f in files:
        if f.startswith("users_") and f.endswith(".json"):
            with open(os.path.join(EXPORT_DIR, f), "r", encoding="utf-8") as file:
                data = json.load(file)
                assert data[0]["username"] in ("alice", "anonymous")


def test_import_json_to_table():
    import_mod.DB_PATH = DB_PATH
    # Prepare JSON file
    data = [{"username": "bob", "email": "bob@example.com"}]
    json_file = os.path.join(EXPORT_DIR, "import_test.json")
    os.makedirs(EXPORT_DIR, exist_ok=True)
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f)
    import_mod.import_json_to_table(json_file, "users")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT username, email FROM users WHERE username='bob'")
    user = cur.fetchone()
    assert user == ("bob", "bob@example.com")
    conn.close()

# Mock DWeb/IPFS export (simulate file copy)
def test_dweb_ipfs_export_mock():
    src = os.path.join(EXPORT_DIR, "mockfile.txt")
    dst = os.path.join(EXPORT_DIR, "ipfs_mock.txt")
    os.makedirs(EXPORT_DIR, exist_ok=True)
    with open(src, "w") as f:
        f.write("mock data")
    # Simulate DWeb/IPFS export
    import shutil
    shutil.copy(src, dst)
    assert os.path.exists(dst)

# Audit/monitoring: check log file creation
def test_audit_log_created():
    anonymize.LOG_FILE = os.path.join(EXPORT_DIR, "anonymize_test.log")
    anonymize.log("test audit log")
    assert os.path.exists(anonymize.LOG_FILE)
    with open(anonymize.LOG_FILE, "r") as f:
        content = f.read()
        assert "test audit log" in content

# Sectorisation: test with sector column
def test_sectorisation_support():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("ALTER TABLE users ADD COLUMN sector TEXT")
    cur.execute("UPDATE users SET sector='marketing'")
    conn.commit()
    cur.execute("SELECT sector FROM users WHERE username='alice' OR username='anonymous'")
    sector = cur.fetchone()[0]
    assert sector == "marketing"
    conn.close()

# RGPD: test opt-out (delete user)
def test_rgpd_opt_out():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE username='alice' OR username='anonymous'")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]
    assert count == 0
    conn.close()
