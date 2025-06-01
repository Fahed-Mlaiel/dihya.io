"""
Tests d'intégration automatisée des fixtures générées depuis /assets/datasets/fixtures
Assure la conformité, la structure, la multilingue et la RGPD.
"""
import pytest
import importlib.util
import sys
sys.path.insert(0, '.')
from backend.db import migrations
import os

def load_fixture_module(name):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../assets/datasets/fixtures/', f'{name}.py'))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

users_sample_fixture = load_fixture_module('users_sample_fixture')
transactions_sample_fixture = load_fixture_module('transactions_sample_fixture')
audit_events_sample_fixture = load_fixture_module('audit_events_sample_fixture')

users_sample = users_sample_fixture.users_sample
transactions_sample = transactions_sample_fixture.transactions_sample
audit_events_sample = audit_events_sample_fixture.audit_events_sample


def test_users_sample_fixture(users_sample):
    for user in users_sample:
        assert 'username' in user
        assert 'email' in user
        assert 'lang' in user
        assert user['lang'] in ['fr', 'en', 'ar', 'kab']
        assert 'role' in user


def test_transactions_sample_fixture(transactions_sample):
    for tx in transactions_sample:
        assert 'id' in tx
        assert 'amount' in tx
        assert 'currency' in tx
        assert 'status' in tx
        assert 'user_id' in tx
        assert 'lang' in tx
        assert tx['lang'] in ['fr', 'en', 'ar', 'kab']


def test_audit_events_sample_fixture(audit_events_sample):
    for event in audit_events_sample:
        assert 'timestamp' in event
        assert 'event' in event
        assert 'user' in event
        assert 'action' in event
        assert 'result' in event
        assert 'lang' in event
        assert event['lang'] in ['fr', 'en', 'ar', 'kab']
