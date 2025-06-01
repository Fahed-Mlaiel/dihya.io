"""
Tests unitaires pour les helpers de chiffrement/déchiffrement (app.security.crypto) — Dihya Coding.

Vérifie le chiffrement AES-256-GCM, le déchiffrement, la gestion des clés et la robustesse face aux erreurs.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import os
import pytest
from base64 import b64encode
from backend.flask.app.securite import crypto

def generate_key():
    """Génère une clé AES-256 aléatoire encodée en base64."""
    return b64encode(os.urandom(32)).decode()

def test_encrypt_decrypt_cycle(monkeypatch):
    """Test le chiffrement et déchiffrement d'une donnée simple."""
    key = os.urandom(32)
    plaintext = "secret à protéger"
    ciphertext, nonce, tag = crypto.encrypt_data(plaintext, key)
    decrypted = crypto.decrypt_data(ciphertext, key, nonce, tag)
    assert decrypted == plaintext

def test_encrypt_decrypt_bytes(monkeypatch):
    """Test le chiffrement et déchiffrement de bytes."""
    key = os.urandom(32)
    plaintext = b"binaire"
    ciphertext, nonce, tag = crypto.encrypt_data(plaintext, key)
    decrypted = crypto.decrypt_data(ciphertext, key, nonce, tag)
    assert decrypted == plaintext.decode()

def test_decrypt_with_wrong_key():
    """Test que le déchiffrement échoue avec une mauvaise clé."""
    key = os.urandom(32)
    wrong_key = os.urandom(32)
    plaintext = "donnée sensible"
    ciphertext, nonce, tag = crypto.encrypt_data(plaintext, key)
    with pytest.raises(Exception):
        crypto.decrypt_data(ciphertext, wrong_key, nonce, tag)

def test_get_crypto_key_env(monkeypatch):
    """Test la récupération de la clé depuis l'environnement."""
    key = generate_key()
    monkeypatch.setenv("CRYPTO_KEY", key)
    key_bytes = crypto.get_crypto_key("CRYPTO_KEY")
    assert isinstance(key_bytes, bytes)
    assert len(key_bytes) == 32

def test_get_crypto_key_invalid(monkeypatch):
    """Test la gestion d'une clé absente ou invalide."""
    monkeypatch.delenv("CRYPTO_KEY", raising=False)
    with pytest.raises(ValueError):
        crypto.get_crypto_key("CRYPTO_KEY")
    # Mauvaise taille
    monkeypatch.setenv("CRYPTO_KEY", b64encode(os.urandom(10)).decode())
    with pytest.raises(ValueError):
        crypto.get_crypto_key("CRYPTO_KEY")
