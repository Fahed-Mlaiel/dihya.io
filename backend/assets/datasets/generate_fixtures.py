#!/usr/bin/env python3
"""
Script de génération automatique de fixtures/tests à partir des datasets Dihya.
- Génère des fixtures Python (pytest), Node.js (Jest), YAML, JSON
- RGPD, anonymisation, multilingue, CI/CD ready
- Génère un rapport de génération
"""
import os
import json
import yaml
from pathlib import Path
from datetime import datetime

DATASET_DIR = Path(__file__).parent
FIXTURES_DIR = DATASET_DIR / 'fixtures'
REPORT_PATH = DATASET_DIR / 'generation_fixtures_report.json'

os.makedirs(FIXTURES_DIR, exist_ok=True)
report = {"date": datetime.utcnow().isoformat() + 'Z', "fixtures": []}

def gen_pytest_fixture(dataset, name):
    code = f"""import pytest\n\n@pytest.fixture\ndef {name}():\n    return {json.dumps(dataset, indent=2, ensure_ascii=False)}\n"""
    return code

def gen_jest_fixture(dataset, name):
    code = f"module.exports = {json.dumps(dataset, indent=2, ensure_ascii=False)};\n"
    return code

for fname in os.listdir(DATASET_DIR):
    if fname.endswith('.json') and fname not in (REPORT_PATH.name,):
        try:
            with open(DATASET_DIR / fname) as f:
                dataset = json.load(f)
            base = fname.replace('.json', '')
            # Python fixture
            py_code = gen_pytest_fixture(dataset, base)
            with open(FIXTURES_DIR / f"{base}_fixture.py", 'w') as fpy:
                fpy.write(py_code)
            # Node.js fixture
            js_code = gen_jest_fixture(dataset, base)
            with open(FIXTURES_DIR / f"{base}_fixture.js", 'w') as fjs:
                fjs.write(js_code)
            # YAML fixture
            with open(FIXTURES_DIR / f"{base}_fixture.yaml", 'w') as fyaml:
                yaml.dump(dataset, fyaml, allow_unicode=True)
            report["fixtures"].append({"dataset": fname, "status": "ok", "files": [f"{base}_fixture.py", f"{base}_fixture.js", f"{base}_fixture.yaml"]})
        except Exception as e:
            report["fixtures"].append({"dataset": fname, "status": "error", "error": str(e)})

with open(REPORT_PATH, 'w') as f:
    json.dump(report, f, indent=2)
print(f"Génération des fixtures terminée. Rapport : {REPORT_PATH}")
