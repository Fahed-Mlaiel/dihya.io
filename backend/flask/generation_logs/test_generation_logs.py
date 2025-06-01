"""
Tests avancés pour la traçabilité des générations de code (Dihya Coding)
"""
import os
import json
import pytest
from backend.flask.generation_logs import log_generation_event, LOG_FILE

def test_log_generation_event_creates_log(tmp_path):
    os.environ['GENERATION_LOG_FILE'] = str(tmp_path / 'generation.log')
    log_generation_event('backend', user='testuser', meta={'stack': 'Flask'})
    with open(os.environ['GENERATION_LOG_FILE'], encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) == 1
    entry = json.loads(lines[0])
    assert entry['event_type'] == 'backend'
    assert entry['user'] == 'testuser'
    assert entry['meta']['stack'] == 'Flask'
    assert 'timestamp' in entry and 'event_id' in entry

def test_log_generation_event_no_user(tmp_path):
    os.environ['GENERATION_LOG_FILE'] = str(tmp_path / 'generation.log')
    log_generation_event('frontend')
    with open(os.environ['GENERATION_LOG_FILE'], encoding='utf-8') as f:
        entry = json.loads(f.readline())
    assert entry['event_type'] == 'frontend'
    assert entry['user'] is None
    assert isinstance(entry['meta'], dict)

# Test de sécurité : pas de secrets dans les logs
@pytest.mark.parametrize('meta', [
    {'password': 'secret'},
    {'api_key': '123'},
    {'token': 'abc'}
])
def test_no_sensitive_data_in_logs(tmp_path, meta):
    os.environ['GENERATION_LOG_FILE'] = str(tmp_path / 'generation.log')
    log_generation_event('backend', user='testuser', meta=meta)
    with open(os.environ['GENERATION_LOG_FILE'], encoding='utf-8') as f:
        entry = json.loads(f.readline())
    for key in meta:
        assert key not in entry['meta'] or entry['meta'][key] != meta[key]
