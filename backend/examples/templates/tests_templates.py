# tests_templates.py – Tests ultra avancés pour tous les templates métiers Dihya
import pytest
from finance_template import process_financial_record
from industrie_template import process_industrie_record
from rh_template import process_rh_record
from sante_template import process_medical_record

def test_finance_anonymization():
    data = {'id': 1, 'client': 'Dupont', 'iban': 'FR76...', 'montant': 1000, 'email': 'a@b.com'}
    result = process_financial_record(data, 'financier1', 'fr')
    assert 'client' not in result['anonymized']
    assert 'iban' not in result['anonymized']
    assert 'email' not in result['anonymized']
    assert result['status'] == 'processed'

def test_industrie_anonymization():
    data = {'id': 1, 'client': 'UsineX', 'site': 'Paris', 'email': 'c@d.com'}
    result = process_industrie_record(data, 'indus1', 'fr')
    assert 'client' not in result['anonymized']
    assert 'site' not in result['anonymized']
    assert 'email' not in result['anonymized']
    assert result['status'] == 'processed'

def test_rh_anonymization():
    data = {'id': 1, 'nom': 'Martin', 'prenom': 'Jean', 'email': 'e@f.com', 'adresse': '1 rue X', 'poste': 'RH'}
    result = process_rh_record(data, 'rh1', 'fr')
    assert 'nom' not in result['anonymized']
    assert 'prenom' not in result['anonymized']
    assert 'email' not in result['anonymized']
    assert 'adresse' not in result['anonymized']
    assert result['status'] == 'processed'

def test_sante_anonymization():
    data = {'id': 1, 'nom': 'Dupont', 'prenom': 'Marie', 'adresse': '2 rue Y', 'email': 'g@h.com', 'diagnostic': 'OK'}
    result = process_medical_record(data, 'medecin1', 'fr')
    assert 'nom' not in result['anonymized']
    assert 'prenom' not in result['anonymized']
    assert 'adresse' not in result['anonymized']
    assert 'email' not in result['anonymized']
    assert result['status'] == 'processed'
