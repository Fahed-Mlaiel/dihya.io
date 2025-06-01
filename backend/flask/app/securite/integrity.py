"""
Module de vérification d’intégrité des données pour Dihya Coding.

Ce module fournit des fonctions pour garantir l’intégrité des données critiques (hash, signature, contrôle de cohérence)
et détecter toute altération ou corruption, conformément aux exigences de sécurité et de conformité RGPD.
"""

import hashlib
import hmac
from typing import Union

def hash_data(data: Union[str, bytes], salt: Union[str, bytes] = "") -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    if isinstance(salt, str):
        salt = salt.encode("utf-8")
    return hashlib.sha256(salt + data).hexdigest()

def verify_hash(data: Union[str, bytes], expected_hash: str, salt: Union[str, bytes] = "") -> bool:
    return hash_data(data, salt) == expected_hash

def hmac_sign(data: Union[str, bytes], secret: Union[str, bytes]) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    if isinstance(secret, str):
        secret = secret.encode("utf-8")
    return hmac.new(secret, data, hashlib.sha256).hexdigest()

def verify_hmac(data: Union[str, bytes], signature: str, secret: Union[str, bytes]) -> bool:
    return hmac.compare_digest(hmac_sign(data, secret), signature)
