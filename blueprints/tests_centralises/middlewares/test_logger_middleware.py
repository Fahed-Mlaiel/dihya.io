"""
Test ultra avancé pour le blueprint logger_middleware (Python)
"""
from blueprints.middlewares.logger_middleware import generate_logger_middleware
import io
import sys

def test_logger_middleware():
    middleware = generate_logger_middleware("Inventaire")
    class DummyRequest:
        method = 'GET'
        path = '/test'
    request = DummyRequest()
    captured = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = captured
    try:
        middleware(request)
    finally:
        sys.stdout = sys_stdout
    output = captured.getvalue()
    assert "[Inventaire] GET /test" in output
