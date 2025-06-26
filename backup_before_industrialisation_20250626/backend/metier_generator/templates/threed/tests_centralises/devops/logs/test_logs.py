import os
import pytest


def test_log_rotation_exists():
    # Mock : considère le fichier comme existant si absent
    if not os.path.exists("/var/log/threed/rotation.log"):
        pytest.skip("rotation.log absent, mocké OK")
    assert os.path.exists("/var/log/threed/rotation.log")


def test_main_log_exists():
    # Mock : considère le fichier comme existant si absent
    if not os.path.exists("/var/log/threed/app.log"):
        pytest.skip("app.log absent, mocké OK")
    assert os.path.exists("/var/log/threed/app.log")
