# test___init__.py – Tests helpers core (Python)
import importlib.util
import os
spec = importlib.util.spec_from_file_location(
    "helper_core",
    "/workspaces/dihya.io/backend/components/metiers/recherche/fixtures/helpers/core/helper_core.py"
)
helper_core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper_core)

def test_core_business_logic():
    assert helper_core.core_business_logic(2, 3) == 5
