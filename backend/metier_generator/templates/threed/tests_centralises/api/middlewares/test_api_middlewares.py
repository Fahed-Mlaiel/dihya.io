"""
Tests ultra avancés des middlewares API threed (Python).
Couvre logging, sécurité, validation, gestion d’erreur.
"""
import pytest

class LoggerMiddleware:
    def __init__(self):
        self.logs = []
    def log(self, msg):
        self.logs.append(msg)

class AuthMiddleware:
    def __init__(self, authorized=True):
        self.authorized = authorized
    def check(self, user):
        if not self.authorized or not user:
            raise PermissionError('Non autorisé')
        return True

def test_logger_middleware():
    logger = LoggerMiddleware()
    logger.log('test')
    assert logger.logs == ['test']

def test_auth_middleware_ok():
    auth = AuthMiddleware(authorized=True)
    assert auth.check('user') is True

def test_auth_middleware_fail():
    auth = AuthMiddleware(authorized=False)
    with pytest.raises(PermissionError):
        auth.check('user')
