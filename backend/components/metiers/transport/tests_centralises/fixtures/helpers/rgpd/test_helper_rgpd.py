# test___init__.py – Tests helpers rgpd (Python)

import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "helper_rgpd",
    "/workspaces/dihya.io/backend/components/metiers/transport/fixtures/helpers/rgpd/helper_rgpd.py",
)
helper_rgpd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper_rgpd)


def test_anonymize_data():
    data = {"a": 1, "b": 2}
    anonymized = helper_rgpd.anonymize_data(data)
    assert anonymized == {"a": "***", "b": "***"}
