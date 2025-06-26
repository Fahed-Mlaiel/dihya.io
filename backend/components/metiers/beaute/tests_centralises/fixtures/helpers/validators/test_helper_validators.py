import importlib.util
import os
spec = importlib.util.spec_from_file_location(
    "helper_validators",
    "/workspaces/dihya.io/backend/components/metiers/beaute/fixtures/helpers/validators/helper_validators.py"
)
helper_validators = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper_validators)

# test___init__.py – Tests helpers validators (Python)
def test_is_valid_email():
    assert helper_validators.is_valid_email("test@example.com")
    assert not helper_validators.is_valid_email("invalid-email")
