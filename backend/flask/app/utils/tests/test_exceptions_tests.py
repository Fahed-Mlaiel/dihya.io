"""
Tests unitaires pour les exceptions personnalisées Dihya Coding.

Vérifie la conformité des exceptions métier, la sécurité des messages,
et la robustesse de la gestion des erreurs dans l’API.
"""

import pytest
from backend.flask.app.utils import exceptions

def test_dihya_error_default():
    err = exceptions.DihyaError()
    assert isinstance(err, Exception)
    assert err.code == 500
    assert "Dihya" in str(err)

def test_validation_error():
    with pytest.raises(exceptions.ValidationError) as exc:
        raise exceptions.ValidationError("Erreur de validation test")
    assert exc.value.code == 422
    assert "validation" in str(exc.value).lower()

def test_auth_error():
    with pytest.raises(exceptions.AuthError) as exc:
        raise exceptions.AuthError("Authentification requise")
    assert exc.value.code == 401
    assert "authentification" in str(exc.value).lower()

def test_permission_error():
    with pytest.raises(exceptions.PermissionError) as exc:
        raise exceptions.PermissionError("Permission refusée")
    assert exc.value.code == 403
    assert "permission" in str(exc.value).lower()

def test_quota_exceeded_error():
    with pytest.raises(exceptions.QuotaExceededError) as exc:
        raise exceptions.QuotaExceededError("Quota dépassé")
    assert exc.value.code == 429
    assert "quota" in str(exc.value).lower()

def test_not_found_error():
    with pytest.raises(exceptions.NotFoundError) as exc:
        raise exceptions.NotFoundError("Ressource non trouvée")
    assert exc.value.code == 404
    assert "trouvée" in str(exc.value).lower()

def test_no_sensitive_data_in_exception():
    # Vérifie qu'aucun message d'exception ne contient de données sensibles
    sensitive = "motdepasse=secret"
    err = exceptions.DihyaError(sensitive)
    assert "motdepasse" not in str(err).lower()
    assert "secret" not in str(err).lower()