"""
Test de cohérence entre la map métiers et la présence effective des fichiers de tests (CI/CD).
"""
import os
import pytest
from metiers_tests_map import METIERS_TESTS_MAP

@pytest.mark.parametrize("metier, test_files", METIERS_TESTS_MAP.items())
def test_metier_tests_exist(metier, test_files):
    for rel_path in test_files:
        abs_path = os.path.join(os.path.dirname(__file__), rel_path)
        assert os.path.isfile(abs_path), f"Test file missing for {metier}: {rel_path}"
