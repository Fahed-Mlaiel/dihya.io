import importlib.util
import os
spec = importlib.util.spec_from_file_location(
    "helper_security",
    "/workspaces/dihya.io/backend/components/metiers/beaute/fixtures/helpers/security/helper_security.py"
)
helper_security = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper_security)

# test___init__.py – Tests helpers security (Python)
def test_hash_password():
    assert helper_security.hash_password("abc") == helper_security.hash_password("abc")
