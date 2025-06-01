"""
Helpers de chiffrement/déchiffrement pour Dihya Coding.

Ce module centralise les fonctions de sécurité cryptographique : chiffrement symétrique, HMAC, génération de clés, etc.
Respecte les bonnes pratiques RGPD et OWASP.
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes, hmac
from cryptography.hazmat.backends import default_backend
from typing import Union, Tuple
from base64 import b64encode, b64decode
import os

def get_crypto_key(env_var: str = "CRYPTO_KEY") -> bytes:
    """
    Récupère la clé de chiffrement depuis une variable d'environnement.

    Args:
        env_var (str): Nom de la variable d'environnement.

    Returns:
        bytes: Clé de chiffrement.

    Raises:
        ValueError: Si la clé est absente ou invalide.
    """
    key = os.environ.get(env_var)
    if not key:
        raise ValueError(f"La clé de chiffrement '{env_var}' est requise.")
    key_bytes = b64decode(key) if not isinstance(key, bytes) else key
    if len(key_bytes) not in (16, 24, 32):
        raise ValueError("La clé doit faire 128, 192 ou 256 bits (16, 24 ou 32 octets).")
    return key_bytes

def encrypt_data(plaintext: Union[str, bytes], key: bytes) -> Tuple[str, str, str]:
    """
    Chiffre une donnée avec AES-256-GCM.

    Args:
        plaintext (str|bytes): Donnée à chiffrer.
        key (bytes): Clé de chiffrement (32 octets recommandé).

    Returns:
        Tuple[str, str, str]: (ciphertext base64, nonce base64, tag base64)
    """
    if isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return (
        b64encode(ciphertext).decode(),
        b64encode(nonce).decode(),
        b64encode(encryptor.tag).decode()
    )

def decrypt_data(ciphertext_b64: str, key: bytes, nonce_b64: str, tag_b64: str) -> str:
    """
    Déchiffre une donnée AES-256-GCM.

    Args:
        ciphertext_b64 (str): Donnée chiffrée (base64).
        key (bytes): Clé de chiffrement.
        nonce_b64 (str): Nonce utilisé (base64).
        tag_b64 (str): Tag d'authentification (base64).

    Returns:
        str: Donnée déchiffrée (texte clair).

    Raises:
        Exception: Si la décryption échoue.
    """
    ciphertext = b64decode(ciphertext_b64)
    nonce = b64decode(nonce_b64)
    tag = b64decode(tag_b64)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode("utf-8")
