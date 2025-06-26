# test_helper_audit.py – Tests helpers audit (Python)
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "helper_audit",
    "/workspaces/dihya.io/backend/components/metiers/seo/fixtures/helpers/audit/helper_audit.py",
)
helper_audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper_audit)


def test_log_audit_event(capsys):
    helper_audit.log_audit_event("event")
    captured = capsys.readouterr()
    assert "AUDIT: event" in captured.out
