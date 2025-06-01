import subprocess, os
import pytest
import glob
import json
import csv

SCRIPTS = [
    'check_integrity',
    'audit_rgpd',
    'audit_accessibilite',
    'audit_logs',
    'audit_plugins',
    'audit_webhooks',
]

SCRIPT_ROOT = os.path.dirname(os.path.abspath(__file__))

@pytest.mark.parametrize('script', SCRIPTS)
def test_audit_script(script):
    result = subprocess.run(['python3', 'main.py', script], cwd=SCRIPT_ROOT, capture_output=True, text=True)
    assert result.returncode == 0, f"Script {script} failed: {result.stderr}"
    assert 'rapport' in result.stdout.lower() or 'report' in result.stdout.lower(), f"No report generated for {script}"

@pytest.mark.parametrize('report_file', [
    'audit_logs_report.csv',
    'audit_logs_report.json',
    'audit_rgpd_report.csv',
    'audit_rgpd_report.json',
    'audit_webhooks_report.csv',
    'audit_webhooks_report.json',
    'audit_accessibilite_report.csv',
    'audit_accessibilite_report.json',
    'check_integrity_report.csv',
    'check_integrity_report.json',
    'audit_plugins_report.csv',
    'audit_plugins_report.json',
])
def test_report_file_exists(report_file):
    path = os.path.join(SCRIPT_ROOT, report_file)
    assert os.path.isfile(path), f"Le rapport {report_file} n'a pas été généré."

@pytest.mark.parametrize('json_report', glob.glob(os.path.join(SCRIPT_ROOT, '*_report.json')))
def test_json_report_structure(json_report):
    with open(json_report) as f:
        data = json.load(f)
        assert isinstance(data, list), f"Le rapport {json_report} doit être une liste."
        assert len(data) > 0, f"Le rapport {json_report} ne contient aucune entrée."

@pytest.mark.parametrize('csv_report', glob.glob(os.path.join(SCRIPT_ROOT, '*_report.csv')))
def test_csv_report_structure(csv_report):
    with open(csv_report) as f:
        reader = csv.reader(f)
        header = next(reader)
        assert len(header) >= 2, f"Le rapport CSV {csv_report} doit avoir au moins 2 colonnes."
        rows = list(reader)
        assert len(rows) > 0, f"Le rapport CSV {csv_report} ne contient aucune donnée."

# Test RGPD/auditabilité : aucune donnée personnelle dans les rapports
@pytest.mark.parametrize('json_report', glob.glob(os.path.join(SCRIPT_ROOT, '*_report.json')))
def test_no_personal_data_in_reports(json_report):
    with open(json_report) as f:
        content = f.read().lower()
        forbidden = ['nom réel','adresse','phone','téléphone','numéro','@gmail.com','@yahoo.com','dupont','durand','smith']
        for word in forbidden:
            assert word not in content, f"Donnée personnelle détectée dans {json_report}: {word}"
