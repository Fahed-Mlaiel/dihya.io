# crypto.py – Chiffrement/déchiffrement avancé

from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
cipher = Fernet(KEY)


def encrypt_data(data: bytes) -> bytes:
    return cipher.encrypt(data)


def decrypt_data(token: bytes) -> bytes:
    return cipher.decrypt(token)
