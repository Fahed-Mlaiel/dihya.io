# test___init__.py – Tests helpers accessibility (Python)
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "helper_accessibility",
    "/workspaces/dihya.io/backend/components/metiers/securite/fixtures/helpers/accessibility/helper_accessibility.py",
)
helper_accessibility = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper_accessibility)


def test_is_accessible():
    class Dummy:
        aria_label = "label"

    assert helper_accessibility.is_accessible(Dummy())
