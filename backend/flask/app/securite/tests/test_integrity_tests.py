"""
Tests unitaires pour la vérification d’intégrité des données (app.security.integrity) — Dihya Coding.

Vérifie le hachage, la vérification de hash, la signature HMAC et la vérification de signature.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import pytest
from backend.flask.app.securite import integrity

def test_hash_data_and_verify():
    """Test le hachage et la vérification simple sans sel."""
    data = "valeur"
    digest = integrity.hash_data(data)
    assert integrity.verify_hash(data, digest)
    assert not integrity.verify_hash("autre", digest)

def test_hash_data_with_salt():
    """Test le hachage et la vérification avec sel."""
    data = "valeur"
    salt = "selSecret"
    digest = integrity.hash_data(data, salt)
    assert integrity.verify_hash(data, digest, salt)
    assert not integrity.verify_hash(data, digest, "autreSel")

def test_hmac_sign_and_verify():
    """Test la signature et la vérification HMAC."""
    data = "message"
    secret = "cleSuperSecrete"
    signature = integrity.hmac_sign(data, secret)
    assert integrity.verify_hmac(data, signature, secret)
    assert not integrity.verify_hmac("autre", signature, secret)
    assert not integrity.verify_hmac(data, signature, "cleFausse")

def test_hash_data_bytes():
    """Test le hachage avec des données en bytes."""
    data = b"binaire"
    digest = integrity.hash_data(data)
    assert integrity.verify_hash(data, digest)
