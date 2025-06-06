#!/usr/bin/env python3
"""
Script de lancement centralisé des tests pour le module threed.
- Ajoute le dossier de tests au PYTHONPATH
- Lance pytest sur tous les tests du module
- Affiche un rapport détaillé
"""
import os
import sys
import subprocess

THREED_TESTS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests'))
if THREED_TESTS_PATH not in sys.path:
    sys.path.insert(0, THREED_TESTS_PATH)

os.environ['PYTHONPATH'] = THREED_TESTS_PATH + os.pathsep + os.environ.get('PYTHONPATH', '')

print(f"[INFO] PYTHONPATH={os.environ['PYTHONPATH']}")

result = subprocess.run([
    sys.executable, '-m', 'pytest', 'tests', '--maxfail=50', '--disable-warnings', '-q'
], cwd=os.path.dirname(__file__))

sys.exit(result.returncode)
