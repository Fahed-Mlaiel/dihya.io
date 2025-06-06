"""
exporter.test.py – Tests unitaires Python pour exporter Threed
"""
import os
import json
import csv
from .exporter import export_to_json, export_to_csv, anonymize

def test_export_to_json(tmp_path):
    data = [{'id': 1, 'user': 'Alice'}, {'id': 2, 'user': 'Bob'}]
    file_path = tmp_path / 'test_export.json'
    export_to_json(data, file_path)
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
        assert 'Alice' in content and 'Bob' in content

def test_export_to_csv(tmp_path):
    data = [{'id': 1, 'user': 'Alice'}, {'id': 2, 'user': 'Bob'}]
    file_path = tmp_path / 'test_export.csv'
    export_to_csv(data, file_path)
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
        assert 'Alice' in content and 'Bob' in content and 'id,user' in content

def test_anonymize():
    data = [{'id': 1, 'user': 'Alice'}, {'id': 2, 'user': 'Bob'}]
    anonymized = anonymize(data)
    assert all(row['user'] == 'anonyme' for row in anonymized)

def test_export_empty():
    file_path = 'empty.csv'
    result = export_to_csv([], file_path)
    assert result == file_path
    if os.path.exists(file_path):
        os.remove(file_path)

def test_export_large_data(tmp_path):
    data = [{'id': i, 'user': f'User{i}'} for i in range(1000)]
    file_path_json = tmp_path / 'test_export_large.json'
    file_path_csv = tmp_path / 'test_export_large.csv'
    export_to_json(data, file_path_json)
    export_to_csv(data, file_path_csv)
    with open(file_path_json, encoding='utf-8') as f:
        content = f.read()
        assert all(f'User{i}' in content for i in range(1000))
    with open(file_path_csv, encoding='utf-8') as f:
        content = f.read()
        assert all(f'User{i}' in content for i in range(1000)) and 'id,user' in content

def test_anonymize_edge_case():
    data = [{'id': 1, 'user': None}, {'id': 2, 'user': ''}]
    anonymized = anonymize(data)
    assert all(row['user'] == 'anonyme' for row in anonymized)

def test_export_special_characters(tmp_path):
    data = [{'id': 1, 'user': 'Al!ce'}, {'id': 2, 'user': 'B@b'}]
    file_path_json = tmp_path / 'test_export_special.json'
    file_path_csv = tmp_path / 'test_export_special.csv'
    export_to_json(data, file_path_json)
    export_to_csv(data, file_path_csv)
    with open(file_path_json, encoding='utf-8') as f:
        content = f.read()
        assert 'Al!ce' in content and 'B@b' in content
    with open(file_path_csv, encoding='utf-8') as f:
        content = f.read()
        assert 'Al!ce' in content and 'B@b' in content and 'id,user' in content

def test_export_invalid_data(tmp_path):
    data = "This is not a valid data format"
    file_path = tmp_path / 'test_export_invalid.json'
    try:
        export_to_json(data, file_path)
        exported = True
    except Exception:
        exported = False
    assert not exported

def test_anonymize_performance(benchmark):
    data = [{'id': i, 'user': 'User{i}'} for i in range(10000)]
    benchmark(anonymize, data)
