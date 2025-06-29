import importlib.util
import os
spec = importlib.util.spec_from_file_location(
    "helper_transformers",
    "/workspaces/dihya.io/backend/components/metiers/threed/fixtures/helpers/transformers/helper_transformers.py"
)
helper_transformers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper_transformers)

# test___init__.py – Tests helpers transformers (Python)
def test_to_uppercase():
    assert helper_transformers.to_uppercase("abc") == "ABC"
