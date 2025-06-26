"""
Test ultra avancé pour script_sample.py
"""

from seo.legacy.samples.scripts.script_sample import script_sample


def test_script_execution():
    assert script_sample("backup") == "Script exécuté pour la tâche : backup"


# ...autres tests avancés, edge cases, robustesse...
