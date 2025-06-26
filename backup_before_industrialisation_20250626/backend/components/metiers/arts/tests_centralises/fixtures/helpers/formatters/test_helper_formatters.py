# test___init__.py – Tests helpers formatters (Python)
import importlib.util
import os
spec = importlib.util.spec_from_file_location(
    "helper_formatters",
    "/workspaces/dihya.io/backend/components/metiers/arts/fixtures/helpers/formatters/helper_formatters.py"
)
helper_formatters = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper_formatters)


def test_format_date():
    from datetime import datetime

    dt = datetime(2025, 6, 9, 12, 0, 0)
    assert helper_formatters.format_date(dt) == "2025-06-09T12:00:00"
