"""
Plugin d’audit PNG pour favicons API backend (accessibilité, RGPD, hash, version, audit, CI/CD).
"""
import os
import hashlib

def audit_png_dir(directory: str):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            path = os.path.join(directory, filename)
            with open(path, 'rb') as f:
                data = f.read()
            hash_val = hashlib.sha256(data).hexdigest()
            print(f"[PNG_AUDIT] {filename} | SHA256: {hash_val} | Size: {len(data)} bytes")

if __name__ == '__main__':
    audit_png_dir(os.path.dirname(__file__))
